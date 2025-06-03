"""
Retriever service module for the Employee Search RAG application.

This module handles all vector store and retrieval-related functionality including
document formatting, embedding generation, and similarity search.
"""

import logging
from typing import List, Dict, Any
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.services.data_service import load_employee_docs, format_employee, create_skill_document, create_project_document
from app.core.config import settings
from app.services.data_service import load_employee_docs

logger = logging.getLogger(__name__)



def get_retriever() -> Any:
    """
    Build and return a configured retriever.

    Returns:
        Any: Configured retriever instance.
    """
    try:
        employees = load_employee_docs()
        logger.info(f"Loaded {len(employees)} employees from data source.")
        
        # Create documents with enhanced metadata
        docs = []
        for emp in employees:
            # Create main document
            main_doc = Document(
                page_content=format_employee(emp),
                metadata={
                    "id": emp["id"],
                    "name": emp["name"],
                    "availability": emp["availability"],
                    "skills": emp["skills"],
                    "experience": emp["experience_years"],
                    "projects": emp["projects"],
                    "type": "employee_profile"
                }
            )
            docs.append(main_doc)
            
            # Create skill-specific documents
            for skill in emp["skills"]:
                docs.append(create_skill_document(emp, skill))
                
            # Create project-specific documents
            for project in emp["projects"]:
                docs.append(create_project_document(emp, project))
        
        # Initialize embeddings
        embeddings = HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL,
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )
        
        # Create vector store
        db = FAISS.from_documents(docs, embeddings)
        db.save_local(settings.VECTOR_STORE_PATH)
        
        # Return retriever with hybrid search
        return db.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={
                "k": settings.MAX_RESULTS,
                "score_threshold": settings.SIMILARITY_THRESHOLD,
                "filter": None
            }
        )
        
    except Exception as e:
        logger.error(f"Error building retriever: {str(e)}")
        raise 