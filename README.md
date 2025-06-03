# HR Resource Query Chatbot

## Overview
A Retrieval Augmented Generation (RAG) application for searching and analyzing employee information using natural language queries. This chatbot leverages advanced AI techniques to provide intelligent responses about employee skills, experience, and project history, making it easier for HR teams to find the right resources for projects and initiatives.

## Features
- 🔍 Semantic search over employee skills, projects, and availability
- 🧠 LLM-powered RAG answer generation for HR Queries with Natural Language
- ⚡ Fast similarity search with FAISS indexing
- 🌐 Interactive UI with Streamlit

## Architecture

```
┌─────────────────┐    ┌─────────────────┐
│   Streamlit UI  │    │   FastAPI REST  │
│   (Web App)     │----│      API        │
└─────────-───────┘    └─────────┬───────┘
                                 │
                     -───────────┘
                     │
           ┌─────────▼─────────┐
           │   Application     │
           │      Core         │
           └─────────┬─────────┘
                     │
    ┌────────────────┼────────────────┐
    │                │                │
┌───▼───┐    ┌──────▼──────┐    ┌────▼────┐
│ Data  │    │ Retriever   │    │   LLM   │
│Service│    │   Service   │    │ Service │
└───┬───┘    └──────┬──────┘    └────┬────┘
    │               │                │
┌───▼──-─┐    ┌─────▼-──────┐    ┌───▼-────┐
│Employee│    │    FAISS    │    │ Ollama  │
│ Data   │    │Vector Store │    │   LLM   │
└───────-┘    └─────────────┘    └─────────┘
```

```
.
├── README.md
├── app/
│   ├── api/
│   │   └── main.py              # FastAPI endpoints
│   ├── core/
│   │   ├── config.py            # Configuration settings
│   │   ├── prompts.py           # LLM prompts and templates
│   │   └── schemas.py           # Data models and validation
│   ├── services/
│   │   ├── data_service.py      # Data handling logic
│   │   ├── llm_service.py       # LLM integration
│   │   └── retriever_service.py # Search and retrieval
│   └── streamlit_app.py         # Web UI interface
├── data/
│   └── employees.json           # Employee database
├── employee_faiss_index/
│   ├── index.faiss             # Vector embeddings
│   └── index.pkl               # Metadata index
├── requirements.txt
└── sample.MD
```

## Component Architecture

### 1. Presentation Layer

#### **Streamlit Web Interface** (`streamlit_app.py`)
- Interactive web application for end users
- Real-time query processing and response display
- User-friendly interface for HR teams
- Integrated chat-like experience

#### **FastAPI REST API** (`api/main.py`)
- RESTful endpoints for programmatic access
- JSON-based request/response handling
- Integration-ready for external systems
- Automatic API documentation (Swagger/OpenAPI)

### 2. Core Layer (`core/`)

#### **Configuration Management** (`config.py`)
- Environment-specific settings
- Model parameters and thresholds
- API keys and connection strings
- System-wide constants

#### **Data Schemas** (`schemas.py`)
- Pydantic models for data validation
- Request/response structures
- Employee data models
- Query result formats

#### **Prompt Templates** (`prompts.py`)
- LLM prompt engineering
- Context formatting templates
- Response generation guidelines

### 3. Service Layer (`services/`)

#### **Data Service** (`data_service.py`)
```python
# Core responsibilities:
- Employee data loading and validation
- Data preprocessing and normalization
- Data format conversions for Embedding Documents
```

#### **Retriever Service** (`retriever_service.py`)
```python
# Core responsibilities:
- Document creation with enhanced metadata (employee profiles, skills, projects)
- Vector embedding generation using HuggingFaceEmbeddings
- FAISS vector store creation and persistence
- Similarity search with configurable score thresholds
- Employee data loading and formatting for retrieval
```

#### **LLM Service** (`llm_service.py`)
```python
# Core responsibilities:
- Ollama LLM integration with connection validation
- Question-Answering chain building using LangChain
- Document chain creation and retrieval integration
- LLM configuration management (temperature, context size, stop tokens)
- Service health checking and connectivity validation
- Error handling with detailed logging and connection diagnostics
- Integration with retriever service for RAG functionality
```

### 4. Data Layer

#### **Employee Database** (`data/employees.json`)
- Structured employee information
- Skills, projects, and experience data

#### **Vector Index** (`employee_faiss_index/`)
- **`index.faiss`**: Pre-computed embeddings for fast similarity search
- **`index.pkl`**: Metadata mappings and document references

## Data Flow Architecture

### Query Processing Pipeline

```
User Query
    │
    ▼
┌─────────────────┐
│  Input Parsing  │
│ & Validation    │
└─────────┬───────┘
          │
          ▼
┌─────────────────┐
│  Query Vector   │
│   Generation    │
└─────────┬───────┘
          │
          ▼
┌─────────────────┐
│ Similarity      │
│ Search (FAISS)  │
└─────────┬───────┘
          │
          ▼
┌─────────────────┐
│ Context         │
│ Preparation     │
└─────────┬───────┘
          │
          ▼
┌─────────────────┐
│ LLM Response    │
│ Generation      │
└─────────┬───────┘
          │
          ▼
┌─────────────────┐
│ Response        │
│ Formatting      │
└─────────┬───────┘
          │
          ▼
    User Response
```

## Technology Stack

### **Backend Framework**
- **FastAPI**: Modern, fast web framework for APIs
- **Streamlit**: Rapid web app development for data applications

### **AI/ML Components**
- **LangChain**: RAG pipeline orchestration
- **FAISS**: Efficient vector similarity search
- **Sentence Transformers**: Text embedding generation
- **Ollama**: Local LLM deployment and inference

### **Data Processing**
- **Pydantic**: Data validation and serialization
- **JSON**: Structured data storage
- **Pickle**: Serialized object storage

## Design Patterns

### **Repository Pattern**
Services abstract data access, allowing for easy swapping of data sources without affecting business logic.

### **Dependency Injection**
Core components are injected into services, promoting testability and modularity.

### **Factory Pattern**
LLM and retriever components are created through factory methods, enabling different model configurations.

### **Observer Pattern**
Configuration changes can trigger re-initialization of dependent components.

## Scalability Considerations

### **Horizontal Scaling**
- Stateless service design enables multiple instance deployment
- Load balancing across API endpoints
- Separate scaling of UI and API components

### **Vertical Scaling**
- FAISS index optimization for memory usage
- Batch processing for large query volumes
- Connection pooling for external services

### **Caching Strategy**
- Query result caching for frequently asked questions
- Embedding caching to avoid recomputation
- Model response caching for similar queries

## Security Architecture

### **Data Protection**
- Local LLM deployment eliminates external data exposure
- Input validation and sanitization
- Rate limiting to prevent abuse

### **Access Control**
- API key authentication (planned)
- Role-based access control (planned)
- Audit logging for compliance

## Performance Characteristics

### **Response Times**
- Vector search: < 100ms
- LLM inference: 1-3 seconds
- End-to-end query: 2-5 seconds

### **Throughput**
- Concurrent users: 10-50 (single instance)
- Queries per second: 5-10
- Scalable with horizontal deployment

## Monitoring and Observability

### **Metrics**
- Query response times
- Search accuracy metrics
- System resource utilization
- Error rates and types

### **Logging**
- Structured logging for query processing
- Error tracking and debugging
- Performance monitoring
- User interaction analytics

## Future Architecture Enhancements

### **Microservices Migration**
- Split services into independent containers
- Service mesh for inter-service communication
- Independent scaling and deployment

### **Advanced AI Features**
- Multi-modal search (text, documents, images)
- Conversational memory and context
- Personalized search results
- Real-time learning and adaptation

### **Enterprise Integration**
- LDAP/Active Directory integration
- HRMS system connectors
- Single Sign-On (SSO) support
- API gateway for external access




### 1. `app/services/data_service.py`

Loads and validates employee data from JSON files, preparing it for indexing and search.

### 2. `app/services/retriever_service.py`

Builds and manages the FAISS vector index, performing semantic search and formatting results with metadata.

### 3. `app/services/llm_service.py`

Handles LLM integration, uses prompts to generate answers, manages context, and deals with errors.

### 4. `app/core/`

* `config.py`: Configuration settings (API keys, environment variables).
* `prompts.py`: LLM prompt templates.
* `schemas.py`: Data models for request and response validation.

### 5. `app/api/main.py`

FastAPI backend exposing endpoints, processing queries, formatting responses, and logging errors.

### 6. `app/streamlit_app.py`

Streamlit frontend providing an interactive chatbot UI that connects to the backend.

### 7. `data/employees.json`

Sample employee data used for indexing and retrieval.

### 8. `employee_faiss_index/`

Stores the FAISS vector index and related metadata files for fast search.



## Setup & Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hr-resource-chatbot.git
cd hr-resource-chatbot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start Ollama server:
```bash
ollama run gemma:3b
```

4. Run the application:
```bash
uvicorn main:app --reload
```

## API Documentation

### POST /query
Query the employee database using natural language.

Request:
```json
{
    "query": "Find employees with machine learning experience in healthcare projects"
}
```

Response:
```json
{
    "response": "Based on the search results, I found the following employees...",
    "matches": [
        {
            "name": "Alice Johnson",
            "skills": ["Machine Learning", "Python", "Healthcare"],
            "projects": ["Healthcare ML System"]
        }
    ]
}
```

## AI Development Process

### AI Tools Used
- Cursor AI for code generation and refactoring
- GitHub Copilot for real-time code suggestions
- ChatGPT for architecture discussions and problem-solving

### AI Assistance in Development
- **Planning Phase (20% AI-assisted)**
  - Architecture decisions and system design
  - Technology stack selection
  - API endpoint planning

- **Implementation Phase (60% AI-assisted)**
  - Code generation for boilerplate
  - Implementation of RAG pipeline
  - Vector store integration
  - API endpoint development

- **Testing & Debugging (30% AI-assisted)**
  - Test case generation
  - Bug identification and fixes
  - Performance optimization

### AI-Generated Solutions
- Hybrid search implementation combining FAISS and keyword matching
- Efficient document chunking strategy
- Smart prompt engineering for better response quality

### Manual Solutions
- Custom data validation logic
- Complex error handling scenarios
- Performance optimization for large datasets

## Technical Decisions

### Model Selection
- **Ollama (Local LLM)**
  - Pros: Privacy, no API costs, full control
  - Cons: Limited model options, local resource requirements
  - Decision: Chose Ollama for data privacy and cost control

### Technology Stack
- **FastAPI**: Modern, fast, and easy to use
- **FAISS**: Efficient vector similarity search
- **LangChain**: Flexible RAG pipeline implementation
- **Ollama**: Local LLM deployment

### Trade-offs
- **Performance vs Privacy**: Chose local deployment for data privacy
- **Cost vs Quality**: Selected open-source models to minimize costs
- **Simplicity vs Features**: Focused on core functionality first

## Future Improvements

1. **Authentication & Security**
   - Add OAuth2 authentication
   - Implement role-based access control
   - Add audit logging

2. **Performance Enhancements**
   - Implement caching layer
   - Add batch processing capabilities
   - Optimize vector search

3. **Feature Additions**
   - Support for more LLM providers
   - Enhanced document preprocessing
   - Real-time data synchronization
   - Advanced analytics dashboard

4. **Infrastructure**
   - Containerization with Docker
   - CI/CD pipeline setup
   - Monitoring and metrics
   - Rate limiting

## Demo
[Link to live demo or screenshots to be added]

## Testing

Run the test suite:
```bash
pytest test_rag.py -v
```

## Configuration

Key configuration parameters:
- `score_threshold`: 0.3 (similarity threshold for retrieval)
- `k`: 5 (number of documents to retrieve)
- `model_name`: "sentence-transformers/all-mpnet-base-v2" (embedding model)
- `llm_model`: "gemma3:latest" (Ollama model)

## Error Handling

The application handles various error cases:
- Connection failures to Ollama
- Invalid data formats
- Missing or malformed queries
- Vector store initialization errors

## Performance Considerations

- Uses FAISS for efficient vector search
- Implements document chunking for better retrieval
- Caches embeddings for improved performance
- Uses hybrid search for better recall

## Future Improvements

1. Add authentication and authorization
2. Implement caching layer
3. Add support for more LLM providers
4. Enhance document preprocessing
5. Add batch processing capabilities
6. Implement rate limiting
7. Add monitoring and metrics 