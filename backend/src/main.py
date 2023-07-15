from typing import Union

from fastapi import FastAPI

from auth.config import auth_backend
from auth.schemas import UserRead, UserCreate, UserUpdate
from auth.manager import fastapi_users

app = FastAPI()

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/users/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/users/registration",
    tags=["registration"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
