from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
from huggingface_hub import InferenceClient

class Input(BaseModel):
    api: str
    user_id: str
    model: str
    text: str

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

@app.post("/summarize_cloudflare")
async def summarize_cloudflare(input: Input):
    try:
        api = f"https://api.cloudflare.com/client/v4/accounts/{input.user_id}/ai/run/"
        headers = {"Authorization": f"Bearer {input.api}"}

        inputs = [
            { "role": "system", "content": "You are a helpful assistant" },
            { "role": "user", "content": f"Generate 3 short highlight from following text. Make sure the output in sentence form, not numbering and only show summarization result: {input.text}"}
        ]
        
        payload = { "messages": inputs , 'raw':'true'}
        response = requests.post(f"{api}{input.model}", headers=headers, json = payload)
        output = response.json()
        return output['result']['response'].strip()
    except TypeError:
        return {"message": "Check your api, user_id, and model"}
    except:
        return output

@app.post("/summarize_backup")
async def summarize_backup(input: Input):
    try:
        client = InferenceClient(
            "meta-llama/Llama-3.3-70B-Instruct",
            token="<HF_TOKEN>",
        )

        messages = [
            {"role": "user", "content": f"Generate 3 short highlight from following text. Make sure the output in sentence form, not numbering and only show summarization result: {input.text}"}
        ]
        
        res = client.chat_completion(messages, max_tokens = 500)
        return res.choices[0].message.content.strip()
    
    except:
        return await summarize_cloudflare(input)

@app.post("/summarize")
async def summarize(input: Input):
    try:
        client = InferenceClient(
            "meta-llama/Llama-3.3-70B-Instruct",
            token="<HF_TOKEN>",
        )

        messages = [
            {"role": "user", "content": f"Generate 3 short highlight from following text. Make sure the output in sentence form, not numbering and only show summarization result: {input.text}"}
        ]
        
        res = client.chat_completion(messages, max_tokens = 500)
        
        return res.choices[0].message.content.strip()
    except:
        return await summarize_backup(input)
