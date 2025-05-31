## Start with PHI identifier - Named Entity Recognition (NER) using 
import requests
import gradio as gr

## Deepseek API url
ollamaurl = "http://localhost:11434/api/generate"
def extract_phi_entities(text):
    """
    Extract PHI entities from the given text using a pre-trained model.
    """
    prompt = f"Extract PHI entities from the following text:\n\n{text}\n\nReturn the entities in JSON format."
    payload = {
        "model": "",
        "prompt": prompt,
        "stream": False,
    }
