import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-fr"
headers = {
    "Authorization": f"Bearer {os.getenv('HF_API_TOKEN')}",
    "Content-Type": "application/json"
}

def translate_text(input_str: str) -> str:
    payload = {"inputs": input_str}
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        output = response.json()
        return output[0]["translation_text"]
    else:
        return f"[Error {response.status_code}] {response.text}"
