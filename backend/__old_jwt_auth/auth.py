from datetime import datetime, timedelta, timezone
from typing import Annotated

from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.ext.asyncio.session import AsyncSession

from .. import crud, models
from ..config import settings
from ..database import get_async_session

router = APIRouter(prefix="/__old_jwt_auth", tags=["Auth"])


class Token(BaseModel):
    access_token: str
    token_type: str


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="__old_jwt_auth/token")


async def authenticate_user(
    username: str,
    password: str,
    db: AsyncSession,
) -> models.User | bool:

    user = await crud.get_user_by_username(username=username, db=db)

    if not user:
        return False
    if not password_context.verify(secret=password, hash=user.hashed_password):
        return False

    return user


def create_access_token(data: dict, expires_delta: timedelta) -> str:

    expire_date = datetime.now(timezone.utc) + expires_delta
    data.update({"exp": expire_date})
    encoded_jwt = jwt.encode(
        claims=data,
        key=settings.SECRET_KEY_FOR_SIGN_JWT,
        algorithm=settings.ALGORITHM,
    )
    return encoded_jwt


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: AsyncSession = Depends(get_async_session),
) -> models.User:

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token=token,
            key=settings.SECRET_KEY_FOR_SIGN_JWT,
            algorithms=[settings.ALGORITHM],
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = await crud.get_user_by_username(username=username, db=db)

    if user is None:
        raise credentials_exception

    return user


async def get_current_active_user(
    current_user: Annotated[models.User, Depends(get_current_user)]
) -> models.User:

    if current_user.is_active is False:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


# special endpoint for getting token during __old_jwt_auth
@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: AsyncSession = Depends(get_async_session),
) -> Token:

    # User __old_jwt_auth
    user = await authenticate_user(
        username=form_data.username,
        password=form_data.password,
        db=db,
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # create JWT
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires,
    )
    return Token(access_token=access_token, token_type="bearer")
