from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from deep_translator import GoogleTranslator

class Text(BaseModel):
    text:str
    source: str
    target: str

def split_text_by_sentences(text, max_length=4900):
    sentences = text.split('. ')
    chunks = []
    current_chunk = []
    current_length = 0

    for sentence in sentences:
        sentence_length = len(sentence) + 1 
        if current_length + sentence_length > max_length:
            chunks.append('. '.join(current_chunk) + '.')
            current_chunk = []
            current_length = 0
        
        current_chunk.append(sentence)
        current_length += sentence_length

    if current_chunk:
        chunks.append('. '.join(current_chunk) + '.')

    return chunks

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"message":"Welcome"}

@app.post("/translate")
async def translate(input: Text, max_length = 4900): 
    if(len(input.text) <= max_length): 
        translated = GoogleTranslator(source=input.source, target = input.target).translate(input.text)
        return {"response":translated}
    
    chunks = split_text_by_sentences(input.text)
    sentences = []
    for chunk in chunks:
        if len(chunk) > 4999:
            continue
        else:
            translated = GoogleTranslator(source=input.source, target = input.target).translate(chunk)
            sentences.append(translated)
        
    return {"response":'. '.join(sentences)}
