from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .database import get_async_session
from .models import User
from .schemas import UserSchema

router = APIRouter(prefix="/user", tags=["User"])


@router.post(
    "/",
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
    "/id/{user_id}",
    response_model=UserSchema,
)
async def get_user_by_id(
    user_id: int,
    db: AsyncSession = Depends(get_async_session),
) -> UserSchema:
    return await crud.get_user_by_id(
        user_id=user_id,
        db=db,
    )


@router.get(
    "/name/{user_name}",
    response_model=UserSchema,
)
async def get_user_by_username(
    user_name: str,
    db: AsyncSession = Depends(get_async_session),
) -> UserSchema:
    return await crud.get_user_by_name(
        user_name=user_name,
        db=db,
    )
