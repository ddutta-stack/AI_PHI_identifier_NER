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
        "model": "deepseek-r1:1.5b",
        "prompt": prompt,
        "stream": False,
    }
    response = requests.post(ollamaurl, json=payload)
    if response.status_code == 200:
        return response.json().get("text", "No entities found.")
    else:
        return f"Error: {response.status_code} - {response.text}"
    ## TEsing the function
    if __name__ == "__main__":
        sample_test_text = "John Doe's phone number is 123-456-7890 and his email is abc@xyz.com and his SSN is 123-45-6789. His patient id is : 21231234"
        print("Testing extract_phi_entities function...")
        result = extract_phi_entities(sample_test_text)
        print("Result:", result)
