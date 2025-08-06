from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from api import translate_text  # or hf_translate if you named it so

app = FastAPI()

class TranslationRequest(BaseModel):
    source_lang: str
    target_lang: str
    input_str: str

@app.post("/translate/")
async def translate(request: TranslationRequest):
    try:
        translated = translate_text(
            request.input_str,
            request.source_lang,
            request.target_lang
        )
        return {"translated_text": translated}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
