from sqlalchemy.pool.impl import StaticPool
from sqlmodel import create_engine, SQLModel, Session

# SQLite database URL (change for production)
DATABASE_URL = "sqlite:///:memory:"

# Create engine with connection pooling
engine = create_engine(
    DATABASE_URL,
    connect_args = {"check_same_thread": False},  # Needed for SQLite
    poolclass = StaticPool,
    echo = True  # Log SQL queries (disable in production)
)


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
