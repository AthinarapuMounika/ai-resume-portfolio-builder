from services.ai_service import generate_text

def create_cover_letter(data, job_description):
    prompt = f"""
Write a professional cover letter for the following candidate.

Candidate Info:
{data}

Job Description:
{job_description}

Make it personalized and engaging.
"""
    return generate_text(prompt)