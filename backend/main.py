from fastapi import FastAPI, Depends, Request
from .auth.auth import auth_backend
from fastapi_users import FastAPIUsers

from .auth.manager import get_user_manager
from .auth.models import User
from .auth.schemas import UserRead, UserCreate
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()
current_active_user = fastapi_users.current_user(optional=True, active=True)


@app.get("/auth/jwt/login", response_class=HTMLResponse)
async def test(request: Request, user: User | None = Depends(current_active_user)):
    print(user)
    if user is None:
        return templates.TemplateResponse(
            request=request, name="index.html"
        )
    else:
        return RedirectResponse(url="/protected-route")


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"
