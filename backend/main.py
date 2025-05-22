from fastapi import FastAPI
from dotenv import load_dotenv

from backend.app.api import *

load_dotenv()

api = FastAPI()

api.include_router(index_router)








