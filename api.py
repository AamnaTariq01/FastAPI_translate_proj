import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_API_TOKEN = os.getenv("HF_API_TOKEN")

BASE_URL = "https://api-inference.huggingface.co/models"

headers = {
    "Authorization": f"Bearer {HF_API_TOKEN}",
    "Content-Type": "application/json"
}

# Supported language codes (Helsinki models follow this pattern)
SUPPORTED_LANG_PAIRS = {
    ("en", "fr"): "Helsinki-NLP/opus-mt-en-fr",
    ("en", "de"): "Helsinki-NLP/opus-mt-en-de",
    ("en", "es"): "Helsinki-NLP/opus-mt-en-es",
    ("en", "ar"): "Helsinki-NLP/opus-mt-en-ar",
    ("en", "hi"): "Helsinki-NLP/opus-mt-en-hi",
    
    ("fr", "en"): "Helsinki-NLP/opus-mt-fr-en",
    ("de", "en"): "Helsinki-NLP/opus-mt-de-en",
    ("es", "en"): "Helsinki-NLP/opus-mt-es-en",
    ("ar", "en"): "Helsinki-NLP/opus-mt-ar-en",
    ("hi", "en"): "Helsinki-NLP/opus-mt-hi-en",
}

def translate_text(input_str: str, source_lang: str, target_lang: str) -> str:
    lang_pair = (source_lang.lower(), target_lang.lower())
    
    if lang_pair not in SUPPORTED_LANG_PAIRS:
        return f"[Error] Translation from {source_lang} to {target_lang} not supported."

    model_name = SUPPORTED_LANG_PAIRS[lang_pair]
    url = f"{BASE_URL}/{model_name}"

    payload = {"inputs": input_str}
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        output = response.json()
        return output[0]["translation_text"]
    else:
        return f"[Error {response.status_code}] {response.text}"
