from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# TODO: research
import frontend.pages.router as pages_router
from .auth.auth import router as test_router
from .auth.router import router as auth_router

app = FastAPI()


app.mount("/static", StaticFiles(directory="./frontend/static"), name="static")
templates = Jinja2Templates(directory="./frontend/templates")


app.include_router(auth_router)
app.include_router(test_router)
app.include_router(pages_router.router)


# @app.get("/auth/jwt/login", response_class=HTMLResponse)
# async def test(request: Request):
#     return templates.TemplateResponse(
#         request=request, name="auth_login.html"
#     )
#
#
# @app.get("/auth/register", response_class=HTMLResponse)
# async def test(request: Request):
#     return templates.TemplateResponse(
#         request=request, name="auth_register.html"
#     )
#
#
# @app.get("/success-route")
# async def protected_route(user: User = Depends(current_user)):
#     return f"Hello, {user.email}"
#
#
# @app.get("/unprotected-route")
# async def unprotected_route():
#     return f"Hello, anonym"
