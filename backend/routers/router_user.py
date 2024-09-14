from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.crud import crud_user
from backend.database import get_async_session
from backend.schemas import UserSchema

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
    return await crud_user.create_user(
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
    return await crud_user.get_user_by_id(
        user_id=user_id,
        db=db,
    )


@router.get(
    "/login/{user_login}",
    response_model=UserSchema,
)
async def get_user_by_username(
    user_login: str,
    db: AsyncSession = Depends(get_async_session),
) -> UserSchema:
    return await crud_user.get_user_by_login(
        user_login=user_login,
        db=db,
    )
