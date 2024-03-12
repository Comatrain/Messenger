from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)


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

