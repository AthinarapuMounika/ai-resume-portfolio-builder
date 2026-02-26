def resume_prompt(data):
    return f"""
Create a professional ATS-friendly resume.

Name: {data['name']}
Email: {data['email']}
Skills: {data['skills']}
Projects: {data['projects']}
Experience: {data['experience']}
Target Role: {data['target_role']}

Make it:
- Professional
- Quantified bullet points
- 1-page format
"""