from sqlalchemy import Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db_connect import Base


class MemoryMFile(Base):
    __tablename__ = "memory_mfile"

    memory_id: Mapped[int] = mapped_column(ForeignKey('memory.id'), primary_key=True, nullable=False)
    image_id: Mapped[int] = mapped_column(ForeignKey('image.id'), primary_key=True, nullable=False)


class MFile(Base):
    __tablename__ = "mfile"

    id: Mapped[int] = mapped_column(Integer(), unique=True, primary_key=True, nullable=False, autoincrement=True)
    description: Mapped[str] = mapped_column(String(length=500), nullable=True)
    url: Mapped[str] = mapped_column(String(length=100), nullable=True)


class Memory(Base):
    __tablename__ = "memory"

    id: Mapped[int] = mapped_column(Integer(), unique=True, primary_key=True, nullable=False, autoincrement=True)
    title: Mapped[str] = mapped_column(String(length=50), nullable=False)
    description: Mapped[str] = mapped_column(String(length=500), nullable=True)
    git_url: Mapped[str] = mapped_column(String(length=100), nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    service_url: Mapped[str] = mapped_column(String(length=100), nullable=True)
    is_public: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False, insert_default=True)
    images = relationship('Image', secondary=MFile.__table__)
