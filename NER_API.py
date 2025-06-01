from fastapi import FastAPI, HTTPException
import requests
app = FastAPI()
ollamaurl = "http://localhost:11434/api/generate"   
@app.post("/extract_phi_entities/")
def extract_phi_entities(text: str):
    """
    Extract PHI entities from the given text using a pre-trained model.
    """
    payload = {
        "model": "deepseek-r1:1.5b",
        "prompt": f"Extract PHI entities such as names, phone numbers, email addresses, and social security numbers from the following text:\n\n{text}\n\nReturn the entities in JSON format. If no entities are found, return an empty JSON object.",
        "stream": False,
    }
    response = requests.post(ollamaurl, json=payload)
    return response.json().get("response", "No entities found.")