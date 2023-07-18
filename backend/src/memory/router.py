from typing import Optional, List

from fastapi import APIRouter, Depends, Query, status, Response, UploadFile
from fastapi.params import File
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.src.db_connect import get_async_session
from .models import Memory

router = APIRouter(
    prefix="/memories",
    tags=["Memories"]
)


@router.get("/")
async def get_memory(response: Response,
                     id: Optional[int] = Query(None),
                     user_id: Optional[int] = Query(None),
                     session: AsyncSession = Depends(get_async_session)
                     ):
    result = None
    if id and not user_id:
        result = await session.execute(select(Memory).filter_by(id=id))
    elif user_id and not id:
        result = await session.execute(select(Memory).filter_by(user_id=user_id))
    elif id and user_id:
        result = await session.execute(select(Memory).filter_by(id=id).filter_by(user_id=user_id))
    if result is None or len(result.all()) == 0:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'msg': "no results"}
    response.status_code = status.HTTP_200_OK
    return {'results': result.all(), 'length': len(result.all())}


@router.post("/images")
async def add_memory_image(response: Response,
                           id: Optional[int] = Query(None),
                           session: AsyncSession = Depends(get_async_session),
                           image: UploadFile = File(),
                           ):
    pass
