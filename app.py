from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NameRequest(BaseModel):
    name: str

@app.post("/submit-name/")
async def submit_name(request: NameRequest):
    return {"message": f"Hello, {request.name}!"}

@app.get("/")  # Root endpoint
async def read_root():
    return {"message": "Welcome to the FastAPI app!"}
