from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "HireLens AI Candidate Evaluation Platform"
    database_url: str = "sqlite:///./hirelens.db"
    upload_dir: str = "uploads"
    cors_origins: str = "http://localhost:5173,http://127.0.0.1:5173"
    class Config:
        env_file = ".env"
        case_sensitive = False
settings = Settings()
