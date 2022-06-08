import os
from urllib.parse import quote

import motor.motor_asyncio
from beanie import init_beanie

from src.databases.nosql_databases.models import PriceResult

DB_HOST = os.getenv('NOSQL_DB_HOST')
DB_PORT = os.getenv('NOSQL_DB_PORT')
DB_NAME = os.getenv('NOSQL_DB_NAME')
DB_USER = os.getenv('NOSQL_DB_USER')
DB_PASSWORD = os.getenv('NOSQL_DB_PASSWORD')

MONGODB_URI = f"mongodb://{DB_USER}:%s@{DB_HOST}:{DB_PORT}/{DB_NAME}?authSource=admin"

async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        MONGODB_URI % quote(DB_PASSWORD)
    )

    await init_beanie(database=client[DB_NAME], document_models=[PriceResult])