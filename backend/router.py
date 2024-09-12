from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .database import get_async_session
from .models import User
from .schemas import UserSchema

router = APIRouter(prefix="/pages", tags=["Pages"])


@router.get("/test")
async def get_test():
    return "This is test"


@router.post(
    "/user",
    status_code=201,
    response_model=UserSchema,
)
async def create_user(
    user: UserSchema,
    db: AsyncSession = Depends(get_async_session),
) -> UserSchema:
    return await crud.create_user(
        user=user,
        db=db,
    )


@router.get(
    "/user/{user_id}",
    response_model=UserSchema,
)
async def get_user_by_id(
    user_id: int,
    db: AsyncSession = Depends(get_async_session),
) -> User:
    return await crud.get_user_by_id(
        user_id=user_id,
        db=db,
    )
