from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import smokeTest
import os # Importez os

# SUPPRIMEZ OU COMMENTEZ debugpy EN PROD
# import debugpy
# debugpy.listen(("0.0.0.0", 5678))

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(smokeTest.router, prefix="/smoke-test")

@app.get('/')
def health():
    return {
        "message": "OK 🚀 lala",
        "port_used": os.environ.get("PORT", "8080") # Pour vérifier le port
    }