from fastapi import FastAPI, Query
from crud import get_latest, get_history

app = FastAPI()

@app.get("/latest")
def latest(sensor_id: str):
    """
    GET endpoint to fetch the latest sensor data entry for a given sensor_id
    """
    return get_latest(sensor_id)

@app.get("/history")
def history(sensor_id: str, start: str, end: str):
    """
    GET endpoint to fetch sensor data between start and end timestamps
    """
    return get_history(sensor_id, start, end)
