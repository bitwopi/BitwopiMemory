from typing import Optional

from fastapi import Depends, Request
from fastapi_users import IntegerIDMixin, BaseUserManager, FastAPIUsers
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from .config import SECRET, auth_backend
from .db import User, get_user_db


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")
        return {'status': "success"}


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


async def get_enabled_backends():
    return [auth_backend]


current_active_user = fastapi_users.current_user(active=True, get_enabled_backends=get_enabled_backends)