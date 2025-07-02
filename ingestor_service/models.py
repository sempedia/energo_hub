from sqlalchemy import Column, String, Float, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Base class for SQLAlchemy ORM models
Base = declarative_base()

class SensorData(Base):
    """
    ORM model for sensor_data table
    Stores sensor id, temperature, power output and timestamp
    """
    __tablename__ = 'sensor_data'

    id = Column(Integer, primary_key=True)
    sensor_id = Column(String)
    temperature = Column(Float)
    power_output = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
