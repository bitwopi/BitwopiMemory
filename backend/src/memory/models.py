from sqlalchemy import Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db_connect import Base


class MemoryImage(Base):
    __tablename__ = "memory_image"

    memory_id: Mapped[int] = mapped_column(ForeignKey('memory.id'), primary_key=True)
    image_id: Mapped[int] = mapped_column(ForeignKey('image.id'), primary_key=True)


class Memory(Base):
    __tablename__ = "memory"

    id: Mapped[int] = mapped_column(Integer(), unique=True, primary_key=True, nullable=False, autoincrement=True)
    title: Mapped[str] = mapped_column(String(length=50), nullable=False)
    description: Mapped[str] = mapped_column(String(length=500), nullable=False)
    git_url: Mapped[str] = mapped_column(String(length=100), nullable=False)
    service_url: Mapped[str] = mapped_column(String(length=100), nullable=False)
    is_public: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    images = relationship('Image', secondary=MemoryImage.__table__)


class Image(Base):
    __tablename__ = "image"

    id: Mapped[int] = mapped_column(Integer(), unique=True, primary_key=True, nullable=False, autoincrement=True)
    description: Mapped[str] = mapped_column(String(length=500), nullable=False)
    path: Mapped[str] = mapped_column(String(length=100), nullable=False)
