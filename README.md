
# HireLens — Explainable AI Candidate Evaluation Platform

HireLens is an AI-powered candidate evaluation platform that analyzes how well a resume matches a target job description. Unlike basic ATS checkers that only count keywords, HireLens verifies whether listed skills are supported by project evidence, detects unsupported claims, ranks projects by job relevance, predicts interview risk areas, and generates an explainable readiness report.

---

## Problem Statement

Candidates often add technologies to their resumes without clearly showing where those skills were used. This creates a trust gap during resume screening and technical interviews.

For example, a resume may mention **Kafka**, **Redis**, or **Kubernetes**, but if those skills are not supported by project bullets, the candidate may struggle during interviews.

HireLens solves this by evaluating resumes using an evidence-first approach:

```text
Resume + Job Description
        ↓
Skill Extraction
        ↓
Skill-to-Project Evidence Mapping
        ↓
Unsupported Claim Detection
        ↓
Project-to-JD Relevance Scoring
        ↓
Interview Risk Prediction
        ↓
Explainable Readiness Report
````

---

## Key Improvements

| Problem                    | HireLens Solution                             |
| -------------------------- | --------------------------------------------- |
| Keyword stuffing           | Maps skills to real project evidence          |
| Unsupported resume claims  | Detects weak or unproven technologies         |
| Poor project ordering      | Ranks projects based on job relevance         |
| Generic ATS feedback       | Generates explainable, role-specific insights |
| Weak interview preparation | Predicts likely interview questions           |
| Resume tailoring guesswork | Provides measurable readiness scores          |

---

## Core Features

### 1. Resume Upload and Parsing

Supports resume upload in:

```text
PDF
DOCX
TXT
```

Extracts:

```text
Skills
Projects
Experience
Education
Certifications
Achievements
Resume bullets
```

---

### 2. Job Description Parsing

Extracts important job requirements such as:

```text
Required skills
Preferred skills
Responsibilities
Role type
Experience level
Tools and technologies
Keywords
```

---

### 3. Skill Evidence Graph

Maps each resume skill to supporting project evidence.

Example:

```json
{
  "skill": "Kafka",
  "claim_strength": "HIGH",
  "confidence_score": 0.91,
  "evidence": [
    {
      "project": "Distributed Job Scheduling System",
      "evidence_text": "Implemented Kafka-based worker execution and dead-letter queue handling."
    }
  ]
}
```

This helps identify whether a skill is actually defensible in an interview.

---

### 4. Unsupported Claim Detection

Flags skills that are listed in the resume but not supported by project evidence.

Example:

```json
{
  "skill": "Kubernetes",
  "risk_level": "HIGH",
  "reason": "Kubernetes is listed in skills, but no project evidence or deployment detail was found.",
  "suggestion": "Add a deployment-related project bullet or remove the claim."
}
```

---

### 5. Project-to-JD Relevance Scoring

Scores each project against the target job description.

Example:

```json
{
  "project_relevance": [
    {
      "project": "Distributed Job Scheduling System",
      "score": 91,
      "reason": "Strong match for Kafka, Redis, distributed locking, retries, and backend reliability."
    },
    {
      "project": "Adaptive API Gateway and Rate Limiter",
      "score": 86,
      "reason": "Strong match for REST APIs, Redis, scalability, rate limiting, and fault tolerance."
    }
  ]
}
```

This helps candidates decide which projects should appear first for a specific role.

---

### 6. Candidate Readiness Score

HireLens generates a weighted readiness score instead of a basic ATS score.

Metrics include:

```text
Overall Readiness Score
Skill Match Score
Keyword Match Score
Project Evidence Score
Claim Support Score
Semantic Similarity Score
Interview Readiness Score
Resume Quality Score
```

Example:

```json
{
  "overall_readiness_score": 84,
  "skill_match_score": 88,
  "keyword_match_score": 79,
  "project_evidence_score": 91,
  "claim_support_score": 76,
  "semantic_similarity_score": 82,
  "interview_readiness_score": 80,
  "resume_quality_score": 78
}
```

---

### 7. Interview Risk Prediction

Generates likely interview questions from strong and weak resume claims.

Example:

```json
{
  "topic": "Redis Distributed Locking",
  "risk_level": "MEDIUM",
  "reason": "Redis locking is mentioned in the project and is likely to be discussed in backend interviews.",
  "questions": [
    "Why did you use Redis for distributed locking?",
    "How did you prevent duplicate job execution?",
    "What happens if the Redis lock expires before the job finishes?",
    "How is Redis locking different from database row locking?"
  ]
}
```

---

### 8. Bullet Improvement Engine

Improves weak resume bullets without adding fake claims.

Example:

**Input**

```text
Built backend project using Spring Boot and MySQL.
```

**Output**

```text
Built a Spring Boot backend with REST APIs, MySQL schema design, service-layer validation, Docker deployment, and integration tests for reliable workflow management.
```

---

### 9. RAG-Based Explainable Feedback

Uses a rule-based RAG-style feedback engine to generate role-aware suggestions.

Example feedback:

```text
Your resume is strong for backend roles because Distributed Scheduler and API Gateway provide evidence for Kafka, Redis, REST APIs, and distributed systems. However, Linux and CI/CD are weakly supported and should be added only if used in your implementation.
```

---

### 10. React Dashboard

The frontend allows users to:

```text
Upload resume
Paste job description
Run candidate evaluation
View readiness scores
Inspect skill evidence graph
Check unsupported claims
View project ranking
Review interview risk questions
Improve resume bullets
```

---

## System Architecture

```text
React Frontend
        ↓
FastAPI Backend
        ↓
Resume Parser Service
        ↓
Job Description Parser Service
        ↓
Skill Extraction Service
        ↓
Skill Evidence Graph Service
        ↓
Claim Verification Service
        ↓
Project Relevance Engine
        ↓
Scoring Engine
        ↓
Interview Risk Engine
        ↓
RAG Feedback Engine
        ↓
SQLite / PostgreSQL-Ready Storage
```

---

## Tech Stack

| Layer        | Technology                                        |
| ------------ | ------------------------------------------------- |
| Frontend     | React, Vite, Axios, CSS                           |
| Backend      | Python, FastAPI                                   |
| Database     | SQLite by default, PostgreSQL-ready               |
| AI Logic     | Embeddings, semantic scoring, RAG-style retrieval |
| File Parsing | PyMuPDF, python-docx                              |
| DevOps       | Docker, Docker Compose                            |
| Testing      | Pytest                                            |

---

## API Endpoints

### Health

```http
GET /health
```

### Resume APIs

```http
POST /api/v1/resumes/upload
GET  /api/v1/resumes/{resume_id}
```

### Job Description APIs

```http
POST /api/v1/jobs
GET  /api/v1/jobs/{job_id}
```

### Analysis APIs

```http
POST /api/v1/analysis/run
GET  /api/v1/analysis/{analysis_id}
```

---

## Quick Start

### Run with Docker

```bash
docker compose up --build
```

Frontend:

```text
http://localhost:5173
```

Backend Swagger UI:

```text
http://localhost:8000/docs
```

Health Check:

```text
http://localhost:8000/health
```

---

## Local Backend Setup

```bash
cd backend
python -m venv venv
```

Activate virtual environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run backend:

```bash
uvicorn app.main:app --reload
```

---

## Local Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

## Sample Workflow

### 1. Upload Resume

```http
POST /api/v1/resumes/upload
```

### 2. Create Job Description

```json
{
  "company": "Microsoft",
  "role": "Software Engineer - Backend",
  "description": "We need Java, Spring Boot, Python, SQL, MySQL, Redis, Kafka, REST APIs, Linux, CI/CD, Docker, distributed systems, automation, architecture, unit testing, and debugging skills."
}
```

### 3. Run Analysis

```json
{
  "resume_id": 1,
  "job_id": 1
}
```

### 4. View Readiness Report

```http
GET /api/v1/analysis/1
```

---

## Example Analysis Output

```json
{
  "overall_readiness_score": 84,
  "skill_match_score": 88,
  "keyword_match_score": 79,
  "project_evidence_score": 91,
  "claim_support_score": 76,
  "semantic_similarity_score": 82,
  "interview_readiness_score": 80,
  "resume_quality_score": 78,
  "missing_keywords": ["Linux", "CI/CD", "Unit Testing"],
  "feedback": "Strong match. Top aligned project: Distributed Job Scheduling System. Unsupported claims: Kubernetes. Missing keywords: Linux, CI/CD, Unit Testing."
}
```

---

## Project Structure

```text
HireLens-AI-Candidate-Evaluation-Platform/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   │
│   ├── tests/
│   ├── uploads/
│   ├── sample_data/
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── styles/
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── Dockerfile
│
├── docker-compose.yml
├── README.md
└── RESUME_LATEX.md
```

---

## Testing

Run backend tests:

```bash
cd backend
pytest
```

The test suite covers:

```text
Skill scoring
Keyword scoring
Overall readiness score calculation
Core scoring engine behavior
```



## What This Project Demonstrates

* FastAPI backend development
* React frontend development
* Resume and JD parsing
* Evidence-based skill validation
* Semantic similarity scoring
* RAG-style explainable feedback
* REST API design
* Dockerized full-stack setup
* Scoring engine design
* Interview preparation automation
* Product-oriented AI system design

---

## Future Enhancements

* JWT authentication
* PostgreSQL + pgvector persistent vector search
* Redis caching
* Async analysis jobs
* Recruiter mode with multi-candidate ranking
* Resume version comparison
* PDF report export
* Prometheus and Grafana observability
* OpenAI/Ollama LLM integration
* Company-specific readiness templates

---

## Author

**Kunal Kumar**

* GitHub: [github.com/kunal7216](https://github.com/kunal7216)
* LinkedIn: [linkedin.com/in/kunal7216](https://www.linkedin.com/in/kunal7216)




