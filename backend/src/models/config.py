"""Configuration management using pydantic-settings"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
import os
from pathlib import Path
from dotenv import load_dotenv


# Find and load the .env file
def load_environment():
    """Load environment variables from .env file"""
    current_dir = Path(__file__).resolve().parent
    # Go up to project root (from backend/src/models/ to project root)
    # backend/src/models/ -> backend/src/ -> backend/ -> project root
    project_root = current_dir.parent.parent.parent
    env_file = project_root / ".env"
    
    if env_file.exists():
        load_dotenv(env_file)
        return True
    return False


# Load environment variables
load_environment()


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # API Keys
    tavily_api_key: str
    groq_api_key: str
    
    # Model Configuration
    model: str = "llama-3.3-70b-versatile"
    
    # Search Configuration
    max_results: int = 5
    
    # Citation Configuration
    citation_style: str = "APA"
    
    model_config = SettingsConfigDict(
        case_sensitive=False,
        extra="ignore"
    )


# Global settings instance
settings = Settings()
