import os
import requests
from dotenv import load_dotenv
load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")

def fetch_serper_results(query):
    url = "https://google.serper.dev/search"
    headers = {"X-API-KEY": SERPER_API_KEY}
    body = {"q": query}
    response = requests.post(url, json=body, headers=headers)
    data = response.json()
    return data.get("organic", [])[:3]  # top 3 results