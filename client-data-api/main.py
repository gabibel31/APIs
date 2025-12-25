from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Client(BaseModel):
    id: int
    name: str
    email: str | None

class ClientsRequest(BaseModel):
    clients: List[Client]

@app.get("/")
def root():
    return {"message": "API is running 🚀"}

@app.post("/clean-clients")
def clean_clients(data: ClientsRequest):
    cleaned = []
    seen_emails = set()

    removed_empty_email = 0
    removed_duplicates = 0

    for client in data.clients:
        # email vide
        if not client.email:
            removed_empty_email += 1
            continue

        # doublon
        if client.email in seen_emails:
            removed_duplicates += 1
            continue

        seen_emails.add(client.email)
        cleaned.append(client)

    return {
        "cleaned_clients": cleaned,
        "stats": {
            "removed_empty_email": removed_empty_email,
            "removed_duplicates": removed_duplicates
        }
    }