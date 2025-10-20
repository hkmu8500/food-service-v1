from sqlalchemy.pool.impl import StaticPool
from sqlmodel import create_engine, SQLModel, Session
from dotenv import load_dotenv
from sqlalchemy import text
import os

load_dotenv()

vercel_env = os.environ.get('VERCEL_ENV', 'local')

if vercel_env == 'local':
    DATABASE_URL = "sqlite:///:memory:"
    # Create engine with connection pooling
    engine = create_engine(
        DATABASE_URL,
        connect_args = {"check_same_thread": False},  # Needed for SQLite
        poolclass = StaticPool,
        echo = True  # Log SQL queries (disable in production)
    )
else:
    TURSO_DATABASE_URL = os.environ.get("TURSO_DATABASE_URL")
    TURSO_AUTH_TOKEN = os.environ.get("TURSO_AUTH_TOKEN")
    engine = create_engine(
        f"sqlite+{TURSO_DATABASE_URL}?secure=true",
        connect_args={
            "auth_token": TURSO_AUTH_TOKEN,
        },
        poolclass = StaticPool,
        echo = True)
    
    drop_all_tables()

def get_db_session():
    """Dependency that provides a DB session for each request"""
    with Session(engine) as session:
        yield session

def get_db_session_sync():
    """Get a database session directly for use in synchronous code (e.g., startup scripts)."""
    return Session(engine)


def create_tables():
    """Create all database tables"""
    SQLModel.metadata.create_all(engine)


def drop_all_tables():
    """Drop all database tables"""
    SQLModel.metadata.drop_all(engine)