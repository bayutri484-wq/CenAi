
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_FILE = BASE_DIR / "cenai.db"


SQLALCHEMY_DATABASE_URL = (
    f"sqlite:///{DATABASE_FILE}"
)


print("DATABASE:")
print(DATABASE_FILE)


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base = declarative_base()