from pydantic import BaseModel
from typing import Optional, List
from app.models.exampleitem import ExampleItemModel

class ExampleItemCollection(BaseModel):
    """
    A container holding a list of `ExampleItemModel` instances.
    """

    exampleitems: List[ExampleItemModel]


class UpdateExampleItemModel(BaseModel):
    """
    A set of optional updates to be made to a document in the database.
    """
    
    title: Optional[str] = None
    code: Optional[str] = None
    value: Optional[int] = None
    description: Optional[str] = None
    model_config = {
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "example": {
                "title": "Lorem ipsum",
                "value": 100,
                "code": "LIPS01",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            }
        },
    }