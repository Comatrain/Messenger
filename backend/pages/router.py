from typing import Annotated

from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from .. import models
from ..auth.auth import get_current_user

router = APIRouter(prefix="/pages", tags=["Pages"])


templates = Jinja2Templates(directory="./frontend/templates")


@router.get("/home")
def get_home_page(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})


@router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


@router.get("/search")
def get_search_page(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})


@router.get("/chat")
def get_chat_page(
    current_user: Annotated[models.User, Depends(get_current_user)],
    request: Request,
):
    if current_user:
        print("yes")
    else:
        print("no")
    return templates.TemplateResponse("chat.html", {"request": request})
