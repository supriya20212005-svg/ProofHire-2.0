# HireLens — Explainable AI Candidate Evaluation Platform

HireLens is a FAANG-style AI + backend platform that evaluates whether a candidate's resume is defensible for a target role. Unlike basic ATS checkers, it verifies whether skills are backed by project evidence, ranks projects against the job description, detects unsupported claims, predicts interview risk, and generates an explainable readiness report.

## Problem Solved

Candidates often list technologies without clear project evidence. This creates a trust gap during resume screening and interviews. HireLens solves this by mapping skills to proof, detecting risky claims, and showing which projects best match a job.

## What It Improves

| Problem | Improvement |
|---|---|
| Keyword stuffing | Evidence-based skill validation |
| Unsupported skills | Claim verification and risk level |
| Wrong project ordering | Project-to-JD ranking |
| Vague feedback | Explainable readiness report |
| Poor interview preparation | Interview risk questions |

## Metrics Generated

- Overall Readiness Score
- Skill Match Score
- Keyword Match Score
- Project Evidence Score
- Claim Support Score
- Semantic Similarity Score
- Interview Readiness Score
- Resume Quality Score

## Core Features

1. Resume upload and parsing — PDF, DOCX, TXT.
2. Job description parsing — skills, responsibilities, role type, keywords.
3. Skill Evidence Graph — maps every skill to project proof.
4. Unsupported Claim Detection — flags skills with weak/no evidence.
5. Project-to-JD Relevance Scoring — ranks projects for a target role.
6. Candidate Readiness Score — weighted scoring beyond basic ATS.
7. Interview Risk Prediction — likely questions from resume claims.
8. Bullet Improvement Engine — improves weak bullets without fake claims.
9. RAG-Based Explainable Feedback — role-aware guidance from rules.
10. React Dashboard — upload, analyze, and view results.

## Architecture

```text
React Frontend
   ↓
FastAPI Backend
   ↓
Resume Parser → JD Parser → Skill Extractor
   ↓
Skill Evidence Graph → Claim Verifier → Project Relevance Engine
   ↓
Scoring Engine → Interview Risk Engine → RAG Feedback Engine
   ↓
SQLite/PostgreSQL-ready Storage
```

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React, Vite, Axios, CSS |
| Backend | Python, FastAPI |
| Database | SQLite default, PostgreSQL-ready |
| AI Logic | Embeddings, semantic scoring, RAG-style retrieval |
| File Parsing | PyMuPDF, python-docx |
| DevOps | Docker, Docker Compose |
| Testing | Pytest |

## Quick Start

```bash
docker compose up --build
```

Frontend: `http://localhost:5173`

Backend Swagger: `http://localhost:8000/docs`

Health: `http://localhost:8000/health`

## API Endpoints

```http
GET  /health
POST /api/v1/resumes/upload
GET  /api/v1/resumes/{resume_id}
POST /api/v1/jobs
GET  /api/v1/jobs/{job_id}
POST /api/v1/analysis/run
GET  /api/v1/analysis/{analysis_id}
```

## Resume LaTeX Entry

```latex
\resumeProjectHeading
{HireLens -- Explainable AI Candidate Evaluation Platform}
{https://github.com/kunal7216/HireLens-AI-Candidate-Evaluation-Platform}
{Python, FastAPI, React, PostgreSQL, pgvector, RAG, Redis, Docker, REST APIs}
\resumeItemListStart
\resumeItem{Candidates often list skills without defensible project evidence; built an explainable AI evaluation platform that maps resume skills to proof, detects unsupported claims, and generates role-specific readiness reports.}
\resumeItem{Improved resume-role alignment by scoring skill match, keyword coverage, project evidence, claim support, semantic similarity, and interview readiness instead of relying on simple ATS keyword matching.}
\resumeItem{Designed FastAPI and React workflows for resume upload, JD parsing, project-to-role ranking, interview risk prediction, bullet improvement, and audit-ready candidate evaluation reports.}
\resumeItemListEnd
```

## Future Enhancements

- JWT auth
- PostgreSQL + pgvector persistent vector search
- Redis caching
- Async analysis jobs
- Recruiter mode with multi-candidate ranking
- PDF report export
- Prometheus/Grafana observability
