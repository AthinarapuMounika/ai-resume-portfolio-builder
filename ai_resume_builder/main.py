import os
from dotenv import load_dotenv

load_dotenv()


from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models
from services.resume_service import create_resume
from services.cover_letter_service import create_cover_letter
from services.portfolio_service import create_portfolio_content
from services.pdf_service import create_pdf

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/generate-resume/")
def generate_resume(data: dict, db: Session = Depends(get_db)):
    resume_text = create_resume(data)

    new_resume = models.Resume(
        name=data["name"],
        email=data["email"],
        skills=data["skills"],
        projects=data["projects"],
        experience=data["experience"],
        target_role=data["target_role"],
        generated_resume=resume_text
    )

    db.add(new_resume)
    db.commit()

    return {"resume": resume_text}

@app.post("/generate-cover-letter/")
def generate_cover(data: dict):
    return {"cover_letter": create_cover_letter(data["candidate"], data["job_description"])}

@app.post("/generate-portfolio/")
def generate_portfolio(data: dict):
    return {"portfolio": create_portfolio_content(data)}
