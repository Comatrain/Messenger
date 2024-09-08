from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from backend.router import router as pages_router
from .auth.auth import router as auth_router

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


app.include_router(auth_router)
app.include_router(pages_router)
