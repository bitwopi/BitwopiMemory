from pathlib import Path

from dotenv import load_dotenv

import os

load_dotenv()

DATABASE_URL = "sqlite+aiosqlite:///../BMemory_db.db?check_same_thread=False"


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
IMAGES_ROOT = os.path.join(MEDIA_ROOT, 'images')
VIDEO_ROOT = os.path.join(MEDIA_ROOT, 'video')
