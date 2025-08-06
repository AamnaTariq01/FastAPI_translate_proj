from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from api import translate_text

app = FastAPI()

class TranslationRequest(BaseModel):
    input_str: str

@app.post("/translate/")
async def translate(request: TranslationRequest):
    try:
        result = translate_text(request.input_str)
        return {"translated_text": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
