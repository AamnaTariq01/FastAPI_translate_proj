# 🌍 FastAPI Translation API (English ➝ French) using Hugging Face

This project demonstrates how to build a RESTful API using **FastAPI** that translates English text to French using the Hugging Face inference API. It's lightweight, free to use, and designed for learning/practice purposes.

---

## 🚀 Features

- 🔁 Translate English ➝ French using Hugging Face's model
- ⚡ Fast and modern backend with FastAPI
- ☁️ No GPU or paid hosting required — just a free Hugging Face token
- ✅ Live Swagger documentation (`/docs`)
- 🔐 API key managed via `.env` (not exposed)

---

## 📁 Project Structure

project/
├── main.py # FastAPI app entry point
├── api.py # Hugging Face API integration logic
├── run.py # (Optional) Runs server and opens docs automatically
├── requirements.txt # Python dependencies
├── .env # Environment variables (e.g., Hugging Face API key)
└── .gitignore # Files and folders to ignore in version control

---

## 📦 Installation

```bash
# Clone this repository
git clone https://github.com/your-username/fastapi-translate-api.git
cd fastapi-translate-api

# (Optional but recommended) Create virtual environment
python -m venv venv
venv\Scripts\activate        # On Windows
# source venv/bin/activate   # On Linux/Mac

# Install required packages
pip install -r requirements.txt

🔐 API Token Setup
Create a free Hugging Face account: https://huggingface.co/join

Generate a read access token: https://huggingface.co/settings/tokens

Create a .env file in your project directory:

ini
Copy
Edit
HF_API_TOKEN=your_token_here
▶️ Run the Application
bash
Copy
Edit
uvicorn main:app --reload  
Then visit:

arduino
Copy
Edit
http://127.0.0.1:8000/docs
Use the Swagger UI to test your translation API interactively.


