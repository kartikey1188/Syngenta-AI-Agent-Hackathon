import os
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

api = FastAPI()

@api.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug_mode = os.getenv("DEBUG", "false").strip().lower() == "true"

    uvicorn.run("main:api", host="0.0.0.0", port=port, reload=debug_mode)


