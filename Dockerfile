FROM python:3.13-slim

WORKDIR /s

RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    libleptonica-dev

COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "-c", "exec uvicorn backend.main:api --host 0.0.0.0 --port ${PORT:-5000}"]