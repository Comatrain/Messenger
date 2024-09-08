# TODO: Uncomment in future
# import secrets
#
# import bcrypt
# import sqlalchemy.exc
# from fastapi import Request, Depends, HTTPException, Response, APIRouter
# from sqlalchemy.ext.asyncio.session import AsyncSession
# from starlette import status
# from starlette.responses import JSONResponse
#
# from .. import crud, schemas
# from ..database import get_async_session
#
# router = APIRouter(
#     prefix="/auth",
#     tags=["Auth"],
# )
#
#
# # This must be randomly generated
# RANDON_SESSION_ID = "iskksioskassyidd"
#
#
# # This must be a lookup on user database
# USER_CORRECT = ("admin", "admin")
#
# # This must be Redis, Memcached, SQLite, KV, etc...
# SESSION_DB = {}
#
#
# @router.post("/register")
# async def register(
#     user_register_schema: schemas.UserRegisterSchema,
#     db: AsyncSession = Depends(get_async_session),
# ):
#     hash_, salt = hash_password(user_register_schema.password)
#     user_create_schema = schemas.UserCreateSchema(
#         email=user_register_schema.email,
#         username=user_register_schema.username,
#         hashed_password=hash_,
#         salt=salt,
#     )
#     await crud.create_user(user=user_create_schema, db=db)
#     return status.HTTP_201_CREATED
#
#
# @router.post("/login")
# async def login(
#     user_login_schema: schemas.UserLoginSchema,
#     db: AsyncSession = Depends(get_async_session),
# ) -> JSONResponse:
#     # check that user exists
#     try:
#         user_model = await crud.get_user_by_username(
#             username=user_login_schema.username,
#             db=db,
#         )
#     except sqlalchemy.exc.NoResultFound:
#         raise HTTPException(status_code=401)
#
#     # validate password
#     result = validate_password(
#         login_password=user_login_schema.password,
#         db_salt=user_model.salt,
#         db_hash=user_model.hashed_password,
#     )
#     if not result:
#         raise HTTPException(status_code=401)
#
#     # response = RedirectResponse("/", status_code=302)
#
#     # create cookie token
#     cookie_session_schema = schemas.CookieSessionCreateSchema(
#         username_id=user_model.id,
#         cookie=secrets.token_urlsafe(255),
#     )
#
#     # submit cookie to database
#     await crud.create_cookie_session(
#         cookie_session=cookie_session_schema,
#         db=db,
#     )
#
#     # response cookie to user
#     content = {"message": "Come to the dark side, we have cookies"}
#     response = JSONResponse(content=content)
#     response.set_cookie(key="Authorization", value=cookie_session_schema.cookie)
#
#     return response
#
#
# @router.post("/logout")
# async def session_logout(response: Response):
#     response.delete_cookie(key="Authorization")
#     SESSION_DB.pop(RANDON_SESSION_ID, None)
#     return {"status": "logged out"}
#
#
# def get_auth_user(request: Request):
#     """verify that user has a valid session"""
#     session_id = request.cookies.get("Authorization")
#     if not session_id:
#         raise HTTPException(status_code=401)
#     if session_id not in SESSION_DB:
#         raise HTTPException(status_code=403)
#     return True
#
#
# def validate_password(
#     login_password: str,
#     db_salt: bytes,
#     db_hash: bytes,
# ) -> bool:
#     bytes_pw = login_password.encode("utf-8")
#     hash_pw = bcrypt.hashpw(bytes_pw, db_salt)
#
#     if hash_pw == db_hash:
#         return True
#     else:
#         return False
#
#
# def hash_password(password: str) -> tuple[bytes, bytes]:
#     # converting password to array of bytes
#     bytes_pw = password.encode("utf-8")
#
#     # generating the salt
#     salt = bcrypt.gensalt()
#
#     # Hashing the password
#     hash_pw = bcrypt.hashpw(bytes_pw, salt)
#     return hash_pw, salt
#
#
# @router.get("/", dependencies=[Depends(get_auth_user)])
# async def secret():
#     return {"secret": "info"}
