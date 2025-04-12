from sqlalchemy import Column, Integer, String, LargeBinary, Float, Date, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String(50))
    correo = Column(String(500))
    contrasena =  Column(String(200))
    estado = Column(Integer)
    codigo = Column(Integer)

class Productos(Base):
    __tablename__ = 'productos'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150))
    descripcion =  Column(String(250))
    imagen = Column(LONGTEXT)
    categorias = Column(String(100))
    subcategorias =  Column(String(150))
    unidadesDeMedida = Column(String(10))
    precio = Column(Float)
    stock =  Column(Integer)

class Almacen(Base):
    __tablename__ = 'almacen'

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(Integer)
    nombre =  Column(String(50))
    direccion = Column(String(500))
    capacidad = Column(Integer)
    tipo =  Column(String(50))
    responsable = Column(String(50))