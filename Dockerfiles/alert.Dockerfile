FROM python:3.11-slim
WORKDIR /app

# Copy alert_service source code into container
COPY ../alert_service /app

# Install Redis Python client
RUN pip install redis

# Run alert service script that listens for alerts from Redis
CMD ["python", "alerts.py"]
