from pydantic import ValidationError
from app.schemas.categoria import CategoriaCreate

try:
    categoria = CategoriaCreate(nombre="     ")
    print("Categoría creada:", categoria.nombre)

except ValidationError as error:
    for detalle in error.errors():
        print("Campo:", detalle["loc"])
        print("Tipo:", detalle["type"])
        print("Mensaje:", detalle["msg"])