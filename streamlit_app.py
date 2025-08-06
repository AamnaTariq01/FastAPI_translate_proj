import streamlit as st
import requests

# 💡 Configure the FastAPI backend URL
API_URL = "http://127.0.0.1:8000/translate/"

# Available language codes
LANGUAGES = {
    "English": "en",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Arabic": "ar",
    "Hindi": "hi"
}

st.set_page_config(page_title="Multi-Language Translator", layout="centered")
st.title("🌍 Multilingual Translator (FastAPI + Hugging Face)")

# Dropdowns for language selection
col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("Translate from:", list(LANGUAGES.keys()), index=0)
with col2:
    target_lang = st.selectbox("Translate to:", list(LANGUAGES.keys()), index=1)

# Input text
input_text = st.text_area("Enter text to translate", height=150)

# Translate button
if st.button("Translate"):
    if source_lang == target_lang:
        st.warning("Please choose different source and target languages.")
    elif input_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Send POST request to FastAPI
        payload = {
            "source_lang": LANGUAGES[source_lang],
            "target_lang": LANGUAGES[target_lang],
            "input_str": input_text
        }

        try:
            response = requests.post(API_URL, json=payload)
            if response.status_code == 200:
                translated = response.json()["translated_text"]
                st.success("🎯 Translation:")
                st.write(translated)
            else:
                st.error(f"API Error: {response.status_code}")
        except Exception as e:
            st.error(f"Error: {e}")
