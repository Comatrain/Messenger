from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import status

from . import schemas, crud, models
from .database import get_async_session

router = APIRouter(prefix="/pages", tags=["Pages"])


@router.get("/test")
async def get_test():
    return "This is test"


@router.post("/user",     response_model=schemas.UserSchema,)
async def create_user(
    user: schemas.UserSchema,
    db: AsyncSession = Depends(get_async_session),
) -> models.User:
    return await crud.create_user(
        user=user,
        db=db,
    )

@router.get(
    "/user/{user_id}",
    response_model=schemas.UserSchema,
            )
async def get_user_by_id(
    user_id: int,
    db: AsyncSession = Depends(get_async_session),
) -> models.User:
    return await crud.get_user_by_id(
        user_id=user_id,
        db=db,
    )