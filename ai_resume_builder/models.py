from sqlalchemy import Column, Integer, String, Text
from database import Base

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    skills = Column(Text)
    projects = Column(Text)
    experience = Column(Text)
    target_role = Column(String)
    generated_resume = Column(Text)