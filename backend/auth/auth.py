import os
from fastapi_users.authentication import AuthenticationBackend, CookieTransport, JWTStrategy
from dotenv import load_dotenv
from ..config import env_path


cookie_transport = CookieTransport(cookie_name="messenger", cookie_max_age=3600)

load_dotenv(dotenv_path=env_path)
AUTH_SECRET = os.getenv("AUTH_SECRET")
print(AUTH_SECRET)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=AUTH_SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
