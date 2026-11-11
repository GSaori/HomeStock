from pydantic import BaseModel, Field, field_validator

class CategoriaCreate(BaseModel):
    nombre: str = Field(min_length=1, max_length=100)

    @field_validator("nombre", mode="before")
    @classmethod
    def validar_nombre(cls, value):
        if isinstance(value, str):
              return value.strip()
        else:
              return value
        
categoria = CategoriaCreate(nombre="  Limpieza  ")

print(categoria.nombre)
print(len(categoria.nombre))