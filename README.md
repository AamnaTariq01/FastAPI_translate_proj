# 🌍 Multilingual Translator (FastAPI + Hugging Face + Streamlit)

A full-stack translation app that uses **FastAPI** as the backend and **Streamlit** for a simple web interface. It translates text between languages using Hugging Face’s public models — all for free, without training any models.

---

## 🚀 Features

- 🔁 Translate between multiple languages (en, fr, de, es, ar, hi)
- ⚡ FastAPI backend with REST API
- 💻 Streamlit frontend with dropdowns and clean UI
- 🔐 Hugging Face API token secured via `.env`
- ▶️ One-click script to launch backend & frontend together

---

## 📁 Project Structure

project/
├── main.py # FastAPI backend
├── api.py # Translation logic (Hugging Face API)
├── streamlit_app.py # Streamlit frontend
├── run_all.py # Launches backend + frontend together
├── requirements.txt # Dependencies
├── .env # Hugging Face token (not tracked)
└── .gitignore # Ignores venv, .env, etc.

yaml
Copy
Edit

---

## 📦 Installation

```bash
# Clone this repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# (Optional) Set up a virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt
🔐 Setup Hugging Face API Key
Sign up: https://huggingface.co/join

Generate a token: https://huggingface.co/settings/tokens

Create a .env file:

env
Copy
Edit
HF_API_TOKEN=your_token_here
▶️ How to Run the App (Auto Script)
bash
Copy
Edit
python run_all.py
✅ This will:

Start the FastAPI server on http://127.0.0.1:8000

Launch Streamlit on http://localhost:8501

Open it automatically in your browser

🛡️ License
MIT — free to use, modify, and distribute.

Made with ❤️ using FastAPI, Hugging Face, and Streamlit.

yaml
Copy
Edit

---

## 🟢 What to Do Now

1. Copy the above content into your local `README.md`
2. Then commit & push:

```bash
git add README.md
git commit -m "Update README with Streamlit and auto-run info"
git push origin main
