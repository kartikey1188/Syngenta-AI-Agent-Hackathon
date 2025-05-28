from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from pathlib import Path
import os
from google.auth.transport.requests import Request

try:
    load_dotenv() 
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error loading environment variables: {e}")

from agentic_environment.app.api import *
from agentic_environment.app.models.sqlalchemy.models import *
from agentic_environment.app.models.sqlalchemy import engine, Base

BASE_DIR = Path(__file__).resolve().parent.parent

if os.getenv("ENV") == "development":
    try:
        Base.metadata.create_all(bind=engine)
        print("Database tables created/updated.")
    except Exception as e:
        print(f"Error creating/updating database tables: {e}")

api = FastAPI()

# Mounting the API routers
api.include_router(index_router) # Main index router

# Calculating base directory and mounting static files from the frontend folder.
try:
    api.mount("/static", StaticFiles(directory=str(BASE_DIR / "frontend")), name="static")
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error mounting static files: {e}")

print("API is running.")











