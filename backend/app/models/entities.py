from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, JSON, String, Text
from sqlalchemy.sql import func
from app.core.database import Base
class Resume(Base):
    __tablename__ = "resumes"
    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String(255), nullable=False)
    content_type = Column(String(120), nullable=True)
    raw_text = Column(Text, nullable=False)
    parsed_json = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
class JobDescription(Base):
    __tablename__ = "job_descriptions"
    id = Column(Integer, primary_key=True, index=True)
    company = Column(String(255), nullable=False)
    role = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    parsed_json = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
class AnalysisReport(Base):
    __tablename__ = "analysis_reports"
    id = Column(Integer, primary_key=True, index=True)
    resume_id = Column(Integer, ForeignKey("resumes.id"), nullable=False)
    job_id = Column(Integer, ForeignKey("job_descriptions.id"), nullable=False)
    overall_readiness_score = Column(Float, nullable=False)
    skill_match_score = Column(Float, nullable=False)
    keyword_match_score = Column(Float, nullable=False)
    project_evidence_score = Column(Float, nullable=False)
    claim_support_score = Column(Float, nullable=False)
    semantic_similarity_score = Column(Float, nullable=False)
    interview_readiness_score = Column(Float, nullable=False)
    resume_quality_score = Column(Float, nullable=False)
    skill_evidence_graph = Column(JSON, nullable=True)
    unsupported_claims = Column(JSON, nullable=True)
    missing_keywords = Column(JSON, nullable=True)
    project_relevance = Column(JSON, nullable=True)
    interview_risks = Column(JSON, nullable=True)
    improved_bullets = Column(JSON, nullable=True)
    feedback = Column(Text, nullable=True)
    audit_events = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
