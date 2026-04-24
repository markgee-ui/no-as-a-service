from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# This tells the server to allow your React app to talk to it
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

RESPONSES = [
    "No.",
    "Absolutely not.",
    "I'd love to, but no.",
    "Error 403: Permission to say yes denied.",
    "My sources say no.",
    "Hard pass."
]

@app.get("/")
def read_root():
    return {"message": "Welcome to NaaS (No as a Service)"}

@app.get("/no")
def get_no():
    return {"answer": "No"}

@app.get("/maybe")
def get_maybe():
    return {"answer": "Still no, but I thought about it for a second."}

@app.get("/random")
def get_random_no():
    return {"answer": random.choice(RESPONSES)}