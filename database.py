# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Get the current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Create the database URL
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'chatbot.db')}"

# Create engine with proper parameters
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    },
    # Enable SQLite foreign key support
    pool_pre_ping=True,
    echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
