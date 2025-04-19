from pydantic import BaseModel
from typing import Optional

class Usuarios(BaseModel):
     id: Optional[int] = None
     nickname: str
     correo: str
     contrasena: str
     estado: int
     codigo: int
     
     class Config:
       from_attributes = True

class RegisterUser(BaseModel):
     id: Optional[int] = None
     nickname: str
     correo: str
     contrasena: str
     estado: int
     codigo: int

     class Config:
       from_attributes = True

class ModificarUser(BaseModel):
     id: Optional[int] = None
     nickname: str
     correo: str

     class Config:
       from_attributes = True

class Modificarcontrasena(BaseModel):
     contrasena: str

     class Config:
       from_attributes = True

class Productos(BaseModel):
     id: Optional[int] = None
     nombre: str
     descripcion: str
     imagen: str
     categorias: str
     subcategorias: str
     unidadesDeMedida: str
     precio: float
     stock: int
     
     class Config:
       from_attributes = True

class Almacen(BaseModel):
     id: Optional[int] = None
     codigo: int
     nombre: str
     direccion: str
     capacidad: int
     tipo: str
     responsable: str

     class Config:
       from_attributes = True

class respuesta(BaseModel):
     mensaje: str