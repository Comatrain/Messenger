from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession

from . import schemas, models


async def create_account_and_user(
    account: schemas.AccountSchema, user: schemas.UserSchema, db: AsyncSession
) -> (models.Account, models.User):
    model_account = models.Account(**account.model_dump())
    model_user = models.User(**user.model_dump())
    db.add(model_account)
    db.add(model_user)
    await db.commit()
    await db.refresh(model_account)
    await db.refresh(model_user)
    # TODO: return 201


async def get_user_by_id(user_id: int, db: AsyncSession) -> models.User:
    stmt = select(models.User).filter(models.User.id == user_id)
    result = await db.execute(stmt)
    user_model = result.scalars().one()
    # TODO: return user_schema
    return user_model
