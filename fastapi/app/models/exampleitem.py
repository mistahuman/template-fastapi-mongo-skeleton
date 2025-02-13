from typing import Optional
from pydantic import BaseModel, Field
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class ExampleItemModel(BaseModel):
    """
    Model for a exampleitem
    """
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    title: str = Field(..., description="Title of exampleitem")
    value: int = Field(..., description="Value of exampleitem")
    code: str = Field(..., description="Code of exampleitem")
    description: Optional[str] = Field(None, description="Description of exampleitem")

    model_config = {
        "populate_by_name": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "example": {
                "title": "Lorem ipsum",
                "value": 100,
                "code": "LIPS01",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            }
        }
    }