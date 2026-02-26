from services.ai_service import generate_text

def create_portfolio_content(data):
    prompt = f"""
Generate portfolio website content:

Name: {data['name']}
Skills: {data['skills']}
Projects: {data['projects']}

Include:
- About Me
- Skills Section
- Projects Section
- Contact Section
"""
    return generate_text(prompt)