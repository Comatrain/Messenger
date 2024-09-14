from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from backend.routers import router_user, router_company

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router_user.router)
app.include_router(router_company.router)
