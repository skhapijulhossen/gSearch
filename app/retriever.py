from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from data_loader import load_employee_docs

def format_employee(emp):
    return f"ID: {emp['id']}\n" \
           f"Name: {emp['name']}\n" \
           f"Skills: {', '.join(emp['skills'])}\n" \
           f"Experience: {emp['experience_years']} years\n" \
           f"Projects: {', '.join(emp['projects'])}\n" \
           f"Availability: {emp['availability']}"

def build_vector_store():
    employees = load_employee_docs()  # Now returns raw dicts
    print(f"Loaded {len(employees)} employees from data source.")
    
    docs = [
        Document(
            page_content=format_employee(emp),
            metadata={"id": emp["id"], "name": emp["name"], "availability": emp["availability"]}
        )
        for emp in employees
    ]
    
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    db = FAISS.from_documents(docs, embeddings)
    db.save_local("employee_faiss_index")
    
    return db.as_retriever(search_type="similarity", search_kwargs={"k": 5})
