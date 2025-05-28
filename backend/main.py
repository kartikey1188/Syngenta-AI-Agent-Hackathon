from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from pathlib import Path
import os
import vertexai
from google.auth.transport.requests import Request

try:
    load_dotenv()
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error loading environment variables: {e}")

from backend.app.api import *
from backend.app.models.sqlalchemy.models import *
from backend.app.models.sqlalchemy import engine, Base
from backend.credentials import credentials, project_id

# try:
#     vertexai.init(project=project_id, credentials=credentials, location="us-central1")
#     print("Vertex AI initialized successfully")
    
# except Exception as e:
#     print(f"Vertex AI initialization failed: {e}")

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION")
vertexai.init(project=PROJECT_ID, location=LOCATION)

BASE_DIR = Path(__file__).resolve().parent.parent

if os.getenv("ENV") == "development":
    try:
        Base.metadata.create_all(bind=engine)
        print("Database tables created/updated.")
    except Exception as e:
        print(f"Error creating/updating database tables: {e}")

api = FastAPI()

# Mounting the API routers
api.include_router(index_router)

# Calculating base directory and mounting static files from the frontend folder.
try:
    api.mount("/static", StaticFiles(directory=str(BASE_DIR / "frontend")), name="static")
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error mounting static files: {e}")

print("API is running.")











