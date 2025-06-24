import os
import requests
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")

GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=" + GEMINI_API_KEY

def generate_gemini_response(prompt, context):
    payload = {
        "contents": [{
            "parts": [{"text": f"User asked: {prompt}\nContext: {context}"}]
        }]
    }
    response = requests.post(GEMINI_URL, json=payload)
    return response.json()['candidates'][0]['content']['parts'][0]['text']


