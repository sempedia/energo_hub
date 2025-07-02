FROM python:3.11-slim
WORKDIR /app

# Copy api_service source code into container
COPY ../api_service /app

# Install dependencies needed for API service
RUN pip install fastapi uvicorn sqlalchemy psycopg2-binary

# Run FastAPI app with Uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
