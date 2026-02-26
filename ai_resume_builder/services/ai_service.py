from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("AIzaSyArArgZNFIhfLs8H7E85XSkJhf6pdwvalg"))

def generate_text(prompt: str):
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt,
    )
    return response.text