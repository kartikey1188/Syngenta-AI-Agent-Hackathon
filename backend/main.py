from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from pathlib import Path

from backend.app.api import *

load_dotenv()

api = FastAPI()

# Calculating base directory and mounting static files from the frontend folder.
BASE_DIR = Path(__file__).resolve().parent.parent
api.mount("/static", StaticFiles(directory=str(BASE_DIR / "frontend")), name="static")

api.include_router(index_router)








