from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router
from app.core.config import settings
from app.core.database import Base, engine
from app.models.entities import AnalysisReport, JobDescription, Resume
Base.metadata.create_all(bind=engine)
app=FastAPI(title=settings.app_name, description='Explainable AI candidate evaluation platform', version='1.0.0')
origins=[o.strip() for o in settings.cors_origins.split(',') if o.strip()]
app.add_middleware(CORSMiddleware, allow_origins=origins+['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
app.include_router(router)
@app.get('/')
def root(): return {'message':'HireLens API','docs':'/docs','health':'/health'}
