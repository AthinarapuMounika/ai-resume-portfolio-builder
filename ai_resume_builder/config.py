import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATABASE_URL = "sqlite:///./resume.db"   # Use PostgreSQL in production