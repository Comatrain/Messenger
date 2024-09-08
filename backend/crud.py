from fastapi import status
from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession

from . import schemas, models


# TODO: Вов, тут надо нормально сделать
# TODO: чтоб возвращался инстанс pydantic, а не алхимии
async def create_user(
    user: schemas.UserSchema, db: AsyncSession
) -> status.HTTP_201_CREATED:
    db_user = models.User(
        email=user.email,
        username=user.username,
        password=user.password,
        role_id=user.role_id,
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


# TODO: Тут тоже
async def get_user_by_id(user_id: int, db: AsyncSession) -> models.User:
    stmt = select(models.User).filter(models.User.id == user_id)
    result = await db.execute(stmt)
    user_model = result.scalars().one()
    return user_model
