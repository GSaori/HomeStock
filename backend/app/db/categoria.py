import uuid

from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base 

class Categoria(Base):
    __tablename__ = "categorias"
    id:Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key = True,
        default = uuid.uuid4
    )

    hogar_id:Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid = True),
        ForeignKey("hogares.id"),
        nullable = False
    )

    nombre: Mapped[str] = mapped_column(
        String(100),
        nullable = False
    )