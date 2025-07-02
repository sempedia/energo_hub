from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
import os

# Database URL, matches ingestor service DB
DB_URL = os.getenv("DB_URL", "postgresql://postgres:postgres@db:5432/omnivise")
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
session = Session()

def get_latest(sensor_id):
    """
    Query the latest sensor_data row for a specific sensor_id
    """
    query = text("SELECT * FROM sensor_data WHERE sensor_id=:sid ORDER BY timestamp DESC LIMIT 1")
    result = session.execute(query, {"sid": sensor_id}).fetchone()
    return dict(result) if result else {}

def get_history(sensor_id, start, end):
    """
    Query sensor_data rows for a sensor_id between start and end datetime strings
    """
    query = text("""
        SELECT * FROM sensor_data
        WHERE sensor_id=:sid AND timestamp BETWEEN :start AND :end
        ORDER BY timestamp ASC
    """)
    result = session.execute(query, {"sid": sensor_id, "start": start, "end": end}).fetchall()
    return [dict(row) for row in result]
