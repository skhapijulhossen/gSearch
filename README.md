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
- **HuggingFace Transformers**: Text embedding generation
- **Ollama**: Local LLM deployment and inference

### **Data Processing**
- **Pydantic**: Data validation and serialization
- **JSON**: Structured data storage
- **Pickle**: Serialized object storage

## Setup & Installation

### 1. Ollama Setup
```bash
# Install Ollama (if not already installed)
# Visit https://ollama.ai for installation instructions

# Start Ollama server
ollama serve
```
*Keep this terminal running - Ollama server needs to stay active*

```bash
# In a new terminal, pull the Mistral model
ollama pull mistral:7b
```

### 2. Repository Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/hr-resource-chatbot.git
cd hr-resource-chatbot
```

### 3. Environment Setup
```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables (if .env file exists)
# Copy .env.example to .env and configure settings
```

### 4. Run FastAPI Backend
```bash
# Start the FastAPI server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
*Keep this terminal running - Backend API will be available at http://localhost:8000*

### 5. Run Streamlit Frontend
```bash
# Open a new terminal, navigate to project directory and activate venv
cd hr-resource-chatbot
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Run Streamlit application
streamlit run streamlit_app.py
```
*Streamlit app will be available at http://localhost:8501*

## Verification Steps

1. **Check Ollama**: Visit http://localhost:11434/api/tags to see available models
2. **Check FastAPI**: Visit http://localhost:8000/docs for API documentation
3. **Check Streamlit**: Visit http://localhost:8501 for the chat interface

## Troubleshooting

- Ensure all three services (Ollama, FastAPI, Streamlit) are running simultaneously
- Check that ports 8000, 8501, and 11434 are available
- Verify Ollama model is properly loaded before starting other services

## API Documentation

---

### 🔹 POST `/chat`

**Description**:
Query the employee database using **natural language** queries. Backed by a local LLM and RAG pipeline.

**Request Body**:

```json
{
  "query": "Find employees with machine learning experience in healthcare projects"
}
```

**Response**:

```json
{
  "response": "Based on the search results, I found the following employees: Alice, Bob..."
}
```

**Errors**:

* `400 Bad Request`: If the query is empty
* `500 Internal Server Error`: On unexpected issues (LLM failure, etc.)

---

### 🔹 GET `/employees/search`

**Description**:
Search employees using structured filters (skills, name, experience, availability).

**Query Parameters**:

| Parameter        | Type     | Description                                      | Example      |
| ---------------- | -------- | ------------------------------------------------ | ------------ |
| `name`           | `string` | Search by name (partial match)                   | `Alice`      |
| `skills`         | `string` | Comma-separated list of skills                   | `python, ml` |
| `min_experience` | `int`    | Minimum required years of experience             | `3`          |
| `availability`   | `string` | Availability status (`available`, `unavailable`) | `available`  |

**Example**:

```
GET /employees/search?skills=python,ml&min_experience=2&availability=available
```

**Response**:

```json
{
  "total": 2,
  "employees": [
    {
      "name": "Alice Johnson",
      "skills": ["Python", "ML"],
      "experience_years": 4,
      "availability": "available"
    },
    {
      "name": "Bob Singh",
      "skills": ["Python", "Machine Learning"],
      "experience_years": 5,
      "availability": "available"
    }
  ]
}
```

**Errors**:

* `500 Internal Server Error`: If filtering fails or employee data is invalid

---


## AI Development Process


**Q: Which AI tools did you use?**
A: I used **Cursor**, **Claude**, and **ChatGPT**.

---

**Q: How did they help you?**
A:

* Helped with **refactoring code** and making it cleaner.
* Gave **quick fixes** for bugs and errors.
* ChatGPT helped with **improving the project architecture**.

---

**Q: How much of your code was AI-generated?**
A: I wrote the **base or skeleton code myself** to stay in control. Around **the final refactored and improvement code was AI-assisted along with code documentation**, mainly for suggestions and improvements.

---

**Q: Any cool AI-generated solutions?**
A: Nothing very unique.

---

**Q: Where did AI not help?**
A: When building **hybrid search** with LangChain, AI couldn’t fix **compatibility issues**.

---

## Demo
[Link to live demo or screenshots to be added]


## Configuration

Key configuration parameters:
- `score_threshold`: 0.3 (similarity threshold for retrieval)
- `k`: 5 (number of documents to retrieve)
- `model_name`: "sentence-transformers/all-mpnet-base-v2" (embedding model)
- `llm_model`: "mistral:7b" (Ollama model)
Sure! Here's the same **Technical Decisions** section rewritten in simple, natural, layman-friendly English—great for interviews, reports, or casual discussions:

---

### Technical Decisions

**Q: Why did you use Mistral 7B (Ollama) instead of OpenAI’s models?**
A: OpenAI is powerful, but it can get expensive, especially when testing a lot. I used **Mistral 7B with Ollama** because it runs offline and gand performed well still being small in size than OpenAI models. It gave me full control and no extra cost.

---

**Q: What made you choose Ollama?**
A: Ollama was lightweight and easy to set up locally. It allowed faster development without needing internet or worrying about token limits. It was ideal for zero-cost experimentation.

---

**Q: Why did you use HuggingFace Embeddings with FAISS?**
A: I used HuggingFace’s Transformer-based Embeddings with FAISS for vector search. FAISS is a fast and memory-efficient tool for vector search, and together they allowed me to build a robust local retrieval system without needing proprietary or paid services.

---

**Q: How did you balance speed, cost, and privacy?**
A:

**Performance**: While local models aren’t as powerful as GPT-4, Mistral 7B performed well enough for the use case—especially with a clean prompt and quality embeddings.

**Cost**: By avoiding cloud APIs, I cut down significant costs, especially during prototyping where models are called frequently.

**Privacy**: Since everything ran locally—LLM, embeddings, and vector store—sensitive data stayed secure on my machine, which is a big plus for client-facing or internal tools.
---

Let me know if you'd like this turned into a short summary or added to your portfolio project!


## Future Improvements

1. Supabase Integration for Full RAG
2. Hybrid Search
3. Streaming Response