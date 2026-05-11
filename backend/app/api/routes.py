from pathlib import Path
from uuid import uuid4
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session
from app.core.config import settings
from app.core.database import get_db
from app.models.entities import AnalysisReport, JobDescription, Resume
from app.schemas.dtos import AnalysisRequest, AnalysisResponse, JobCreateRequest, JobResponse, ResumeResponse
from app.services.analysis_service import AnalysisService
from app.services.extraction import ExtractionService
from app.services.file_parser import FileParserService
router=APIRouter()
@router.get('/health')
def health_check(): return {'status':'UP','service':'HireLens'}
@router.post('/api/v1/resumes/upload', response_model=ResumeResponse)
async def upload_resume(file: UploadFile = File(...), db: Session = Depends(get_db)):
    suffix=Path(file.filename or '').suffix.lower()
    if suffix not in ['.pdf','.docx','.txt']: raise HTTPException(status_code=400, detail='Only PDF, DOCX, and TXT files are supported')
    upload_dir=Path(settings.upload_dir); upload_dir.mkdir(parents=True, exist_ok=True); saved=upload_dir/f'{uuid4().hex}{suffix}'; saved.write_bytes(await file.read())
    text=FileParserService().parse(str(saved)); parsed=ExtractionService().parse_resume(text); resume=Resume(file_name=file.filename or saved.name, content_type=file.content_type, raw_text=text, parsed_json=parsed)
    db.add(resume); db.commit(); db.refresh(resume); return resume
@router.get('/api/v1/resumes/{resume_id}', response_model=ResumeResponse)
def get_resume(resume_id:int, db:Session=Depends(get_db)):
    r=db.get(Resume,resume_id)
    if not r: raise HTTPException(status_code=404, detail='Resume not found')
    return r
@router.post('/api/v1/jobs', response_model=JobResponse)
def create_job(req:JobCreateRequest, db:Session=Depends(get_db)):
    parsed=ExtractionService().parse_job_description(req.description, req.role); job=JobDescription(company=req.company, role=req.role, description=req.description, parsed_json=parsed)
    db.add(job); db.commit(); db.refresh(job); return job
@router.get('/api/v1/jobs/{job_id}', response_model=JobResponse)
def get_job(job_id:int, db:Session=Depends(get_db)):
    j=db.get(JobDescription,job_id)
    if not j: raise HTTPException(status_code=404, detail='Job description not found')
    return j
@router.post('/api/v1/analysis/run', response_model=AnalysisResponse)
def run_analysis(req:AnalysisRequest, db:Session=Depends(get_db)):
    r=db.get(Resume,req.resume_id); j=db.get(JobDescription,req.job_id)
    if not r: raise HTTPException(status_code=404, detail='Resume not found')
    if not j: raise HTTPException(status_code=404, detail='Job description not found')
    result=AnalysisService().analyze(r.raw_text, r.parsed_json or {}, j.description, j.parsed_json or {})
    report=AnalysisReport(resume_id=r.id, job_id=j.id, **result); db.add(report); db.commit(); db.refresh(report); return report
@router.get('/api/v1/analysis/{analysis_id}', response_model=AnalysisResponse)
def get_analysis(analysis_id:int, db:Session=Depends(get_db)):
    report=db.get(AnalysisReport,analysis_id)
    if not report: raise HTTPException(status_code=404, detail='Analysis report not found')
    return report
