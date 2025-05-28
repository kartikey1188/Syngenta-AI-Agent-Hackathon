from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path

# Calculating base directory and setting the templates directory relative to this file.
BASE_DIR = Path(__file__).resolve().parents[3]
templates = Jinja2Templates(directory=str(BASE_DIR / "frontend"))

index_router = APIRouter()

# @index_router.get("/")
# async def index(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})
