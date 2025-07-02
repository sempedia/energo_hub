from flask import Flask, request, jsonify
from redis import Redis
from models import SensorData
from db import session, init_db

app = Flask(__name__)

# Redis client used to publish alerts when temperature is high
redis_client = Redis(host='redis', port=6379, decode_responses=True)

# Initialize DB and create tables if not exist
init_db()

@app.route("/ingest", methods=["POST"])
def ingest():
    """
    Receives sensor data in JSON format,
    stores it in PostgreSQL,
    and publishes an alert to Redis if temperature > 100.
    """
    data = request.get_json()
    sensor = SensorData(**data)
    session.add(sensor)
    session.commit()

    if data["temperature"] > 100:
        # Publish alert message to Redis 'alerts' channel
        redis_client.publish("alerts", f"🔥 {data['sensor_id']} high temp: {data['temperature']}°C")

    return jsonify({"status": "stored"})

if __name__ == '__main__':
    # Run Flask app on all interfaces on port 5001
    app.run(host="0.0.0.0", port=5001)
