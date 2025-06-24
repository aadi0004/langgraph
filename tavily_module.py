import os
import requests
from dotenv import load_dotenv
load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def fetch_tavily_summary(query):
    url = "https://api.tavily.com/search"
    headers = {"Authorization": f"Bearer {TAVILY_API_KEY}"}
    payload = {"query": query, "search_depth": "basic", "include_answer": True}
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    return data.get("answer", "No summary available.")