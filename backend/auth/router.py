from typing import Annotated

from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession

from .auth import get_current_user, get_current_active_user, authenticate_user
from .utils import hash_password
from .. import crud, models
from ..database import get_async_session
from ..schemas import UserCreateSchema, UserLoginSchema
from urllib.parse import parse_qs

router = APIRouter(prefix="/auth", tags=["Auth"])


templates = Jinja2Templates(directory="./frontend/templates")


@router.get("/register")
def get_register_page(request: Request):
    return templates.TemplateResponse("auth_register.html", {"request": request})


@router.post("/register")
async def create_account(
    user: UserCreateSchema,
    db: AsyncSession = Depends(get_async_session),
):
    user.password = hash_password(user.password)
    await crud.create_user(user=user, db=db)
    return "Account was created. Now go to http://localhost:8000/pages/home"


@router.get("/login")
def get_register_page(request: Request):
    return templates.TemplateResponse("auth_login.html", {"request": request})


@router.post("/login")
async def create_account(
    user: UserLoginSchema,
    db: AsyncSession = Depends(get_async_session),
):
    auth = await authenticate_user(
        username=user.username,
        password=user.password,
        db=db,
    )
    if auth:
        print("yes")
    else:
        print("no")
    return "Account was created. Now go to http://localhost:8000/pages/home"


@router.get("/users/me/")
async def test_read_users_me(
    current_user: Annotated[models.User, Depends(get_current_user)]
):
    return current_user


@router.get("/users/me/items/")
async def test_read_own_items(
    current_user: Annotated[models.User, Depends(get_current_active_user)]
):
    return [{"item_id": "Foo", "owner": current_user.username}]
