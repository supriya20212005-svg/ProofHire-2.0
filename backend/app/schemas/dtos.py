from datetime import datetime
from typing import Any, Optional
from pydantic import BaseModel
class ResumeResponse(BaseModel):
    id: int; file_name: str; content_type: Optional[str] = None; parsed_json: Optional[Any] = None; created_at: datetime
    class Config: from_attributes = True
class JobCreateRequest(BaseModel):
    company: str; role: str; description: str
class JobResponse(BaseModel):
    id: int; company: str; role: str; description: str; parsed_json: Optional[Any] = None; created_at: datetime
    class Config: from_attributes = True
class AnalysisRequest(BaseModel):
    resume_id: int; job_id: int
class AnalysisResponse(BaseModel):
    id: int; resume_id: int; job_id: int
    overall_readiness_score: float; skill_match_score: float; keyword_match_score: float
    project_evidence_score: float; claim_support_score: float; semantic_similarity_score: float
    interview_readiness_score: float; resume_quality_score: float
    skill_evidence_graph: Optional[Any] = None; unsupported_claims: Optional[Any] = None
    missing_keywords: Optional[Any] = None; project_relevance: Optional[Any] = None
    interview_risks: Optional[Any] = None; improved_bullets: Optional[Any] = None
    feedback: Optional[str] = None; audit_events: Optional[Any] = None; created_at: datetime
    class Config: from_attributes = True
