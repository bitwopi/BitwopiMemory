from fastapi import FastAPI, Depends

from config import auth_backend, current_active_user, fastapi_users
from db import User
from schemas import UserCreate, UserRead, UserUpdate


# @app.get("/authenticated-route")
# async def authenticated_route(user: User = Depends(current_active_user)):
#     return {"message": f"Hello {user.email}!"}
