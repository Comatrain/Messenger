from fastapi import FastAPI, Depends, Request, APIRouter
from sqlalchemy import select
from .database import get_async_session
from .models import User
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.get("/")
async def test(is_active: bool, session: AsyncSession = Depends(get_async_session)):
    stmt = (
        select(User)
        .filter(User.is_active == is_active)
    )
    result = await session.execute(stmt)
    return (
        result.scalars()
        .all()
    )
