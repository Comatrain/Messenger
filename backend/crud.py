from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession

from . import schemas, models


async def create_user(user: schemas.UserCreateSchema, db: AsyncSession) -> models.User:
    db_user = models.User(
        email=user.email,
        username=user.username,
        hashed_password=user.hashed_password,
        salt=user.salt,
        role_id=user.role_id,
        is_active=user.is_active,
        is_superuser=user.is_superuser,
        is_verified=user.is_verified,
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def get_user_by_username(username: str, db: AsyncSession) -> models.User:
    stmt = select(models.User).filter(models.User.username == username)
    result = await db.execute(stmt)
    return result.scalars().one()


async def create_cookie_session(
    cookie_session: schemas.CookieSessionCreateSchema,
    db: AsyncSession,
) -> models.CookieSession:
    db_cookie_session = models.CookieSession(**cookie_session.model_dump())
    db.add(db_cookie_session)
    await db.commit()
    await db.refresh(db_cookie_session)
    return db_cookie_session
