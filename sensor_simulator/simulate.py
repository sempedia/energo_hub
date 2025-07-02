import requests
import time
import random

# URL to send simulated sensor data
INGEST_URL = "http://localhost:5001/ingest"
# List of sensor IDs to simulate
SENSOR_IDS = ["sensor-1", "sensor-2"]

while True:
    for sensor_id in SENSOR_IDS:
        # Create random sensor data payload
        payload = {
            "sensor_id": sensor_id,
            "temperature": round(random.uniform(20, 120), 2),
            "power_output": round(random.uniform(50, 500), 2)
        }
        try:
            # Send POST request with sensor data to ingestor service
            res = requests.post(INGEST_URL, json=payload)
            print(f"[{sensor_id}] Sent: {payload}, Status: {res.status_code}")
        except Exception as e:
            print(f"Error sending data: {e}")
    # Wait 10 seconds before next batch
    time.sleep(10)
