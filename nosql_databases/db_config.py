import os
from urllib.parse import quote

import motor.motor_asyncio

DB_HOST = os.getenv('NOSQL_DB_HOST')
DB_PORT = os.getenv('NOSQL_DB_PORT')
DB_NAME = os.getenv('NOSQL_DB_NAME')
DB_USER = os.getenv('NOSQL_DB_USER')
DB_PASSWORD = os.getenv('NOSQL_DB_PASSWORD')

MONGODB_URI = f"mongodb://{DB_USER}:%s@{DB_HOST}:{DB_PORT}/{DB_NAME}?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI % quote(DB_PASSWORD))
db = client.prediction_result

# Dependency
def get_db():
    try:
        yield db
    finally:
        db.close