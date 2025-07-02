# Energo Hub

![Docker](https://img.shields.io/badge/docker-compose-blue?logo=docker)
![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Status](https://img.shields.io/badge/status-prototype-yellow)
<!-- You can add more like CI/CD, License, etc. if applicable -->

A prototype energy-sector IoT + Data Storage platform that unifies everything in one place for the user.

## Features
- Sensor data ingestion using a Flask-based ingestor service
- Real-time alerts via Redis Pub/Sub mechanism
- Time-series sensor data stored in PostgreSQL
- REST API powered by FastAPI to query sensor data
- Microservices architecture, containerized with Docker Compose

## Project Structure

- `sensor_simulator/`: Simulates sensor devices sending data to the ingestor
- `ingestor_service/`: Receives sensor data and stores it; publishes alerts
- `api_service/`: Exposes REST endpoints for querying sensor data
- `alert_service/`: Listens to Redis alerts and prints notifications
- `Dockerfiles/`: Dockerfile definitions for each service
- `docker-compose.yml`: Orchestrates all services and dependencies

## Quick Start

1. Build and start all services:

```bash
docker-compose up --build
```

2. Simulate sensor data by running:

```bash
python sensor_simulator/simulate.py
```
⚙️ Tested with Python 3.10+. Optionally create a virtual environment and install dependencies

```bash
pip install requests
```

3. Query latest sensor data:

```bash
curl "http://localhost:8000/latest?sensor_id=sensor-1"
```

4. Query historical data:

```bash
curl "http://localhost:8000/history?sensor_id=sensor-1&start=2025-07-01T00:00:00&end=2025-07-02T00:00:00"
```

## Notes

- 🗄️ PostgreSQL: `localhost:5432`, database: `omnivise`
- 🔁 Redis: `localhost:6379`
- 📥 Ingestor API: `http://localhost:5001/ingest`
- 🌐 Query API: `http://localhost:8000`
- 🚨 Alerts: Printed to the console by the `alert_service`
