from fastapi import APIRouter, HTTPException, Depends, status
from app.schemas.exampleitem import ExampleItemCollection, UpdateExampleItemModel
from app.models.exampleitem import ExampleItemModel
from app.crud.exampleitem import ExampleItemCRUD
from fastapi.responses import Response
from app.dependencies import get_exampleitem_db


router = APIRouter(prefix="/exampleitems", tags=["exampleitems"])

# POST /exampleitems
@router.post(
    "/", 
    response_description="Add a new exampleitem",
    response_model=ExampleItemModel, 
	response_model_by_alias=False,
)
async def add_exampleitem(example: ExampleItemModel, db: ExampleItemCRUD = Depends(get_exampleitem_db)):
    """ ... """
    return await db.create_exampleitem(example)

# GET /exampleitems
@router.get(
    "/",
    response_description="Get exampleitem collection",
    response_model=ExampleItemCollection,
    response_model_by_alias=False,
)
async def get_exampleitems(db: ExampleItemCRUD = Depends(get_exampleitem_db)):
    """ ... """
    return await db.get_exampleitems()

# GET /exampleitems/{id}
@router.get(
    "/{id}",
    response_description="Get a single exampleitem",
    response_model=ExampleItemModel,
    response_model_by_alias=False,
)
async def show_exampleitem(id: str, db: ExampleItemCRUD = Depends(get_exampleitem_db)):
    """
    Get the record for a specific exampleitem, looked up by `id`.
    """
    example = await db.show_exampleitem(id)
    if example: 
        return example
    
    raise HTTPException(status_code=404, detail=f"ExampleItem {id} not found")

# PATCH /exampleitems/{id}
@router.patch(
    "/{id}",
    response_description="Update a single exampleitem",
    response_model=ExampleItemModel,
    response_model_by_alias=False,
)
async def update_exampleitem(id: str, update_data: UpdateExampleItemModel, db: ExampleItemCRUD = Depends(get_exampleitem_db)):
    """
    Update the record for a specific exampleitem, looked up by `id`.
    """
    example = await db.update_exampleitem(id, update_data)
    if example: 
        return example
    
    raise HTTPException(status_code=404, detail=f"ExampleItem {id} not found")



# DELETE /exampleitems/{id}
@router.delete(
    "/{id}",
    response_description="Delete a exampleitem"
)
async def delete_exampleitem(id: str, db: ExampleItemCRUD = Depends(get_exampleitem_db)):
    """
    Remove a single exampleitem record from the database if not associated to worklog
    """
    delete_result = await db.delete_exampleitem(id)

    if delete_result:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"ExampleItem {id} not found")

