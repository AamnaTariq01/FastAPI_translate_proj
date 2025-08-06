import webbrowser
import subprocess

# Open Swagger UI
webbrowser.open("http://127.0.0.1:8000/docs#/default/translate_translate__post")

# Run the FastAPI server
subprocess.run(["uvicorn", "main:app", "--reload"])
