from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from ..db_connect import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer(), unique=True, primary_key=True, nullable=False, autoincrement=True)
    username: Mapped[str] = mapped_column(String(length=30), unique=True, index=True, nullable=False)
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"User {self.username} with id {self.id}"
