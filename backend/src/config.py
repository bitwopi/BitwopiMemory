from dotenv import load_dotenv

import os

load_dotenv()

DATABASE_URL = "sqlite+aiosqlite:///../BMemory_db.db?check_same_thread=False"
