from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import schemas, crud, models
from .database import get_async_session

router = APIRouter(prefix="/pages", tags=["Pages"])


@router.get("/test")
async def get_test():
    return "This is test"


@router.post(
    "/user",
    response_model=schemas.UserSchema,
)
async def create_user(
    login: str,
    password: str,
    first_name: str,
    last_name: str,
    email: str,
    # TODO: do DRY for None
    company_id: Optional[int] = None,
    db: AsyncSession = Depends(get_async_session),
):
    account_schema = schemas.AccountSchema(login=login, password=password)
    user_schema = schemas.UserSchema(
        account_login=login,
        first_name=first_name,
        last_name=last_name,
        email=email,
        company_id=company_id,
    )
    await crud.create_account_and_user(
        account=account_schema,
        user=user_schema,
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
