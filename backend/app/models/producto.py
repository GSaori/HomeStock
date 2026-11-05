import uuid

from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base 
from sqlalchemy import UniqueConstraint
from sqlalchemy import ForeignKeyConstraint
from sqlalchemy import UniqueConstraint

class Producto(Base):
    __tablename__ = "productos"

    __table_args__ = (
         ForeignKeyConstraint(
                ["hogar_id", "categoria_id"],
                ["categorias.hogar_id", "categorias.id"],
                name="fk_productos_categoria_hogar" #sirve para asignarle un nombre a una restricción de clave foránea (Foreign Key) dentro de la base de datos
            ),
        UniqueConstraint(
            "hogar_id",
            "id",
            name="uq_categorias_hogar_id_id"
        ),
    ) #Llave foreana compuesta

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

    categoria_id:Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid = True),
        nullable = False
    )

    nombre: Mapped[str] = mapped_column(
        String(150),
        nullable = False
    )

    unidad_base: Mapped[str] = mapped_column(
        String(10),
        nullable=False #Hace que el campo sea obligatorio
    )