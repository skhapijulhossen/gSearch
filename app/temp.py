from retriever import build_vector_store

retriever = build_vector_store()

results = retriever.invoke("Available Python developers with AWS")
print(results)
