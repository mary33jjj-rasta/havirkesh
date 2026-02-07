from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, declarative_base

# 🔹 PostgreSQL connection URL
DATABASE_URL = "postgresql://postgres:123456@localhost:5432/DBhavirkesht"

engine = create_engine(
DATABASE_URL,
pool_pre_ping=True, # جلوگیری از قطع شدن connection
echo=True # در صورت نیاز برای دیباگ (در prod False)
)

SessionLocal = sessionmaker(
autocommit=False,
autoflush=False,
bind=engine
)

Base = declarative_base()


def create_db_and_tables():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
            db.close()


SessionDep = Annotated[Session, Depends(get_db)]

from app.models.provinces import Provinces
from app.models.city import Cities
from app.models.village import Villages  
