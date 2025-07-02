from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import os

# Database connection URL, configurable via env variable DB_URL
DB_URL = os.getenv("DB_URL", "postgresql://postgres:postgres@db:5432/omnivise")

# Create engine and session factory
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    """
    Create all tables in the database.
    Called once on service startup.
    """
    Base.metadata.create_all(engine)
