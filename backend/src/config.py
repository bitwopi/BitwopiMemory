from dotenv import load_dotenv

import os

from sqlalchemy.orm import declarative_base

load_dotenv()

DATABASE_URL = "sqlite:///translator_db.db?check_same_thread=False"
BASE = declarative_base()
