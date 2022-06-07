import os
from urllib.parse import quote

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_HOST = os.getenv('SQL_DB_HOST')
DB_PORT = os.getenv('SQL_DB_PORT')
DB_NAME = os.getenv('SQL_DB_NAME')
DB_USER = os.getenv('SQL_DB_USER')
DB_PASSWORD = os.getenv('SQL_DB_PASSWORD')

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:%s@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL % quote(DB_PASSWORD))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()