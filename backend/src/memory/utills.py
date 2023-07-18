import os.path
import string
import uuid
import random

from sqlalchemy.ext.asyncio import AsyncSession

from backend.src.config import IMAGES_ROOT, VIDEO_ROOT
from backend.src.memory.models import Memory, MFile

ALLOWED_EXTENSIONS = {'jpg': IMAGES_ROOT,
                      'jpeg': IMAGES_ROOT,
                      'png': IMAGES_ROOT,
                      'mp4': VIDEO_ROOT}


async def add_memory(session: AsyncSession, **kwargs):
    new_memory = Memory(title=kwargs.get('title'),
                        description=kwargs.get('description'),
                        git_url=kwargs.get('git_url'),
                        user_id=kwargs.get('user_id'),
                        service_url=kwargs.get('service_url'),
                        is_public=kwargs.get('is_public')
                        )
    new_memory.images = save_files(kwargs.get('files'))
    try:
        session.add(new_memory)
        await session.commit()
        print("memory successfully added")
    except Exception as e:
        await session.rollback()
        print(e)


def get_file_extension(filename: str):
    return filename.split(".")[-1].lower()


def generate_random_filename(extension):
    unique_id = str(uuid.uuid4().hex)
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    filename = f"{unique_id}_{random_chars}.{extension}"
    return filename


async def save_files(files: list):
    results = []
    for file in files:
        extension = get_file_extension(file.src.name)
        file_url = f"{ALLOWED_EXTENSIONS[extension]}/{generate_random_filename(extension)}"
        if extension in ALLOWED_EXTENSIONS.keys():
            try:
                with open(file_url, 'wb') as uploaded_file:
                    file_content = await file.src.read()
                    uploaded_file.write(file_content)
                results.append(MFile(description=file.desc, url=file_url))
            except Exception as e:
                print(e)

