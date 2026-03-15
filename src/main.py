from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import smokeTest
import os

app = FastAPI()

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(smokeTest.router, prefix="/smoke-test")

@app.get('/')
def health():
    return {"status": "up", "message": "Deploy Success! 🚀"}