import os
from motor.motor_asyncio import AsyncIOMotorClient
from app.crud.exampleitem import ExampleItemCRUD
from app.conf.config import Config


DB_NAME = Config.app_settings.get('db_name')
MONGO_URI = Config.app_settings.get('mongodb_url')
motor_client = AsyncIOMotorClient(MONGO_URI)

def get_exampleitem_db() -> ExampleItemCRUD:
    db = motor_client[DB_NAME]  
    return ExampleItemCRUD(db)


