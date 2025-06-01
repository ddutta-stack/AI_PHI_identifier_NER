## Start with PHI identifier - Named Entity Recognition (NER) using 
import requests
import gradio as gr

## Deepseek API url
ollamaurl = "http://localhost:11434/api/generate"

def extract_phi_entities(text):
    """
    Extract PHI entities from the given text using a pre-trained model.
    """
    prompt = f"Extract PHI or named entities from the following text:\n\n{text}\n\n Return the entities in JSON format."
    payload = {
        "model": "deepseek-r1:1.5b",
        "prompt": prompt,
        "stream": False,
    }
    response = requests.post(ollamaurl, json=payload)
    if response.status_code == 200:
        return response.json().get("response", "No entities found.")
    else:
        return f"Error: {response.status_code} - {response.text}"


## Create a Gradio interface for the function, so commenting this out !!

# ## TEsting the function
# if __name__ == "__main__":
#         sample_test_text = "John Doe's phone number is 123-456-7890 and his email is abc@xyz.com and his SSN is 123-45-6789."
#         print("Testing extract_phi_entities function...")
#         result = extract_phi_entities(sample_test_text)
#         print("Result:", result)

# Creating the Gradio interface
interface = gr.Interface(
    fn=extract_phi_entities,
    inputs=gr.Textbox(label="Input Text",lines=6, placeholder="Enter text to extract PHI entities..."),
    outputs=gr.JSON(label="Extracted Entities"),
    title="PHI Identifier - Named Entity Recognition (NER)",
    description="This tool extracts PHI entities from the provided text using a pre-trained model.",
)
# Launch the Gradio interface and test the function
if __name__ == "__main__":
    interface.launch(share=True)  # Set share=True to allow public access
    # interface.launch()  # Use this for local testing without public access