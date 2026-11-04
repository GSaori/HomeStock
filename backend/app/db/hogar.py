import uuid
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped,mapped_column
from app.db.base import Base

class Hogar(Base): #DeclarativeBase permite que SQLAlchemy identifique las clases que representan tablas
    __tablename__ = "hogares"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    nombre: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )