from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from app.models.exampleitem import ExampleItemModel
from app.schemas.exampleitem import ExampleItemCollection, UpdateExampleItemModel
from pymongo import ReturnDocument

class ExampleItemCRUD:
    def __init__(self, db: AsyncIOMotorClient) -> None:
        self.db = db
        self.collection = db["exampleitems"]

    async def create_exampleitem(self, task: ExampleItemModel) -> ExampleItemModel:
        new_task = await self.collection.insert_one(task.model_dump(by_alias=True, exclude=["id"]))
        created_task = await self.collection.find_one({"_id": new_task.inserted_id})
        return created_task

    async def get_exampleitems(self) -> ExampleItemCollection:
        return ExampleItemCollection(exampleitems=await self.collection.find().to_list())

    async def show_exampleitem(self, example_id: str) -> ExampleItemModel | None:
        return await self.collection.find_one({"_id": ObjectId(example_id)})

    async def update_exampleitem(self, example_id: str, update_data: UpdateExampleItemModel) -> ExampleItemModel | None:
        new_exampleitem = {
            k: v for k, v in update_data.model_dump(by_alias=True).items() if v is not None
        }
        result = await self.collection.find_one_and_update(
            {"_id": ObjectId(example_id)},
            {"$set": new_exampleitem},
            return_document=ReturnDocument.AFTER
        )
        return result

    async def delete_exampleitem(self, example_id: str) -> bool:
        result = await self.collection.delete_one({"_id": ObjectId(example_id)})
        return result.deleted_count > 0
