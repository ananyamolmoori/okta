'''from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NameRequest(BaseModel):
    name: str

@app.post("/submit-name/")
async def submit_name(name_request: NameRequest):
    return {"message": f"Hello, {name_request.name}!"}'''
