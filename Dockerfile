FROM python:3.13-slim

WORKDIR /app

COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "-c", "cd backend && adk web --host 0.0.0.0 --port ${PORT:-8000}"]

