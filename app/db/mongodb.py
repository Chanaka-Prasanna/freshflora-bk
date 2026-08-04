from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

class MongoDB:
    client: AsyncIOMotorClient = None
    db = None

db_client = MongoDB()

async def connect_to_mongo():
    db_client.client = AsyncIOMotorClient(settings.mongodb_url)
    db_client.db = db_client.client[settings.database_name]
    print("Connected to MongoDB")

async def close_mongo_connection():
    if db_client.client:
        db_client.client.close()
        print("Closed MongoDB connection")
