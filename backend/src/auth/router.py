from fastapi import APIRouter, Depends

from .manager import current_active_user
from .db import User

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.username}!"}
