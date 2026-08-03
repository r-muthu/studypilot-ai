# StudyPilot AI

An AI-powered study assistant that helps students interact with lecture notes, textbooks, and research papers through Retrieval-Augmented Generation (RAG) and an agentic AI workflow.

Users can upload PDF documents, ask natural language questions, and receive context-grounded responses generated from their study materials.

---

## Features

- 📄 Upload PDF lecture notes and research papers
- 🤖 Agentic AI workflow powered by LangGraph
- 🔍 Retrieval-Augmented Generation (RAG)
- 💬 Chat with uploaded documents
- 📚 Multi-document support
- 🧠 Automatic context retrieval using vector similarity search
- 🔄 Conversation memory across a chat session
- 🌐 Full-stack web application
- ☁️ Dockerised backend deployed on AWS EC2
- ⚡ React frontend deployed on Vercel

---

## Tech Stack

### Frontend

- React
- TypeScript
- Vite
- Tailwind CSS
- Axios

### Backend

- FastAPI
- LangChain
- LangGraph
- ChromaDB
- PyMuPDF

### AI

Supports multiple LLM providers through a unified interface:

- OpenAI
- Google Gemini
- Amazon Bedrock

### Deployment

- Docker
- Docker Compose
- AWS EC2
- Vercel

---

## Architecture

```
                        User
                          │
                          ▼
               React Frontend (Vercel)
                          │
                  HTTPS API Requests
                          │
                          ▼
          FastAPI Backend (AWS EC2 Docker)
                          │
              ┌───────────┴───────────┐
              │                       │
         LangGraph Agent         PDF Upload
              │                       │
              ▼                       ▼
        Agent Tools             Text Extraction
              │                       │
              └───────────┬───────────┘
                          ▼
                  Chroma Vector Store
                          │
                          ▼
                   Retrieved Context
                          │
                          ▼
                     LLM Response
```

---

## Agent Workflow

Instead of directly prompting an LLM, StudyPilot uses an agent capable of selecting tools based on the user's request.

Current tools include:

- Retrieve relevant context from uploaded documents
- Retrieve uploaded document names
- Retrieve document-specific context
- Multi-document retrieval
- Context-aware question answering

This allows the agent to dynamically determine the appropriate workflow for tasks such as:

- summarising documents
- answering questions
- comparing documents
- generating quizzes
- explaining concepts

---

## Project Structure

```
backend/
│
├── app/
│   ├── agents/
│   ├── api/
│   ├── rag/
│   ├── services/
│   ├── schemas/
│   ├── models/
│   └── main.py
│
├── uploads/
├── chroma_db/
├── Dockerfile
└── docker-compose.yml

frontend/
│
├── src/
│   ├── components/
│   ├── hooks/
│   ├── services/
│   ├── types/
│   └── App.tsx
│
└── vite.config.ts
```

---

## Getting Started

### Backend

```bash
cd backend

uv sync

uv run uvicorn app.main:app --reload
```

or

```bash
docker compose up --build
```

Backend runs at

```
http://localhost:8000
```

Swagger UI

```
http://localhost:8000/docs
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at

```
http://localhost:5173
```

---

## Environment Variables

Example `.env`

```env
MODEL_PROVIDER=openai

OPENAI_API_KEY=

GOOGLE_API_KEY=

AWS_REGION=

AWS_BEARER_TOKEN_BEDROCK=

BEDROCK_MODEL=
```

---

## Current Capabilities

- Upload PDF documents
- Parse and chunk documents
- Generate embeddings
- Store vectors in ChromaDB
- Retrieve relevant passages
- Agent selects appropriate retrieval workflow
- Multi-turn conversations
- Multiple LLM providers
- Docker deployment
- AWS deployment

---

## Planned Improvements

### Authentication

- User registration and login
- Secure password hashing
- Session or JWT-based authentication

This allows each user's documents and conversations to remain private and enables personalised study workspaces.

### PostgreSQL Integration

Introduce PostgreSQL to persist application data instead of relying solely on in-memory state or local files.

Planned data to store includes:

- User accounts
- Uploaded document metadata
- Conversation history
- User prompts
- Assistant responses
- Conversation timestamps

Persisting chat history allows users to continue previous study sessions, revisit explanations, and provides a foundation for features such as searchable conversations and personalised recommendations.

### Improved User Interface

- Better responsive layout
- Richer chat interface
- Loading states
- Drag-and-drop uploads
- Document management
- Dark mode
- Mobile optimisation

### Dynamic Backend Configuration

Replace the hardcoded backend API endpoint with a configurable environment-based solution.

This allows the frontend to communicate with the appropriate backend instance depending on the deployment environment (development, staging, or production), making the application more portable and easier to deploy across different infrastructure.

### Production Infrastructure

- HTTPS using Nginx and Let's Encrypt
- Custom domain
- Automated CI/CD pipeline
- AWS S3 for document storage
- pgvector migration for scalable vector search
- Background task queue for document processing

---

## Learning Outcomes

This project demonstrates practical experience with:

- Full-stack web development
- REST API design
- Agentic AI workflows
- Retrieval-Augmented Generation (RAG)
- LangChain
- LangGraph
- Vector databases
- Prompt engineering
- Docker containerisation
- AWS cloud deployment
- Modern React development

---

## License

This project is licensed under the MIT License.
