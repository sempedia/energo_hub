# Use slim Python 3.11 base image for smaller size
FROM python:3.11-slim
WORKDIR /app

# Copy ingestor_service source code into container
COPY ../ingestor_service /app

# Install dependencies needed for the ingestor service
RUN pip install flask redis sqlalchemy psycopg2-binary

# Run the ingestor Flask app on container start
CMD ["python", "app.py"]
