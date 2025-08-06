import subprocess
import time
import webbrowser
import os
import platform

# Windows-specific fix for terminal window titles
if platform.system() == "Windows":
    creationflags = subprocess.CREATE_NEW_CONSOLE
else:
    creationflags = 0

# Step 1: Start FastAPI server (main.py on port 8000)
fastapi_process = subprocess.Popen(
    ["uvicorn", "main:app", "--reload"],
    creationflags=creationflags
)

# Step 2: Wait a few seconds to ensure server starts
time.sleep(3)

# Step 3: Start Streamlit frontend
streamlit_process = subprocess.Popen(
    ["streamlit", "run", "streamlit_app.py"],
    creationflags=creationflags
)

# Step 4: Open the frontend in browser
webbrowser.open("http://localhost:8501")

try:
    fastapi_process.wait()
    streamlit_process.wait()
except KeyboardInterrupt:
    print("Shutting down...")
    fastapi_process.terminate()
    streamlit_process.terminate()
