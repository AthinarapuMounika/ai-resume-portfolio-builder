from services.ai_service import generate_text
from utils.prompt_templates import resume_prompt

def create_resume(data):
    prompt = resume_prompt(data)
    return generate_text(prompt)
