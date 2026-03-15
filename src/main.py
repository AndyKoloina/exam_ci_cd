from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

# Import de votre routeur (assurez-vous que le fichier smokeTest.py existe dans le même dossier)
try:
    from . import smokeTest
except ImportError:
    import smokeTest

app = FastAPI(title="Custom FastAPI Service")

# Configuration CORS pour autoriser les requêtes du frontend
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusion du routeur
app.include_router(smokeTest.router, prefix="/smoke-test")

@app.get('/')
def health():
    """Endpoint de santé utilisé par Cloud Run pour vérifier si le conteneur est prêt"""
    return {
        "status": "active",
        "message": "OK 🚀 lala",
        "environment": "production"
    }

# Note: Pas de bloc 'if __name__ == "__main__"' ici. 
# C'est le Dockerfile qui gère le lancement avec Uvicorn.