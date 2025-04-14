from fastapi import APIRouter,HTTPException
from typing import List
from starlette.responses import RedirectResponse
from sqlalchemy.orm import session
from fastapi.params import Depends

from Database.conexion import engine, sessionlocal

import Database.schemas as page_schemas
import Database.conexion as page_conexion
import Database.models as page_models
import random



page_models.Base.metadata.create_all(bind=engine)
router = APIRouter()


def get_product():
    try:
        db = sessionlocal()
        yield db
    finally:
        db.close()

@router.get("/register-product")
async def Main():
    return RedirectResponse(url="/docs/")

@router.get("/ver-product/", response_model=List[page_schemas.Productos])
async def show_product(db:session=Depends(get_product)):
    product = db.query(page_models.Productos).all()
    return product


@router.post("/registrar-productos/",response_model=page_schemas.Productos)
def create_user(entrada:page_schemas.Productos,db:session=Depends(get_product)):
   product = page_models.Productos(nombre = entrada.nombre, 
                                  descripcion= entrada.descripcion, 
                                  imagen = entrada.imagen, 
                                  categorias = entrada.categorias, 
                                  subcategorias = entrada.subcategorias,
                                  unidadesDeMedida = entrada.unidadesDeMedida,
                                  precio = entrada.precio,
                                  stock = entrada.stock)
   db.add(product)
   db.commit()
   db.refresh(product)
   return product

@router.put("/cambiar-producto/{product_id}",response_model=page_schemas.Productos)
def mod_product(productId: int, entrada:page_schemas.Productos,db:session=Depends(get_product)):
    producto = db.query(page_models.Productos).filter_by(id=productId).first()
    producto.nombre = entrada.nombre 
    producto.descripcion= entrada.descripcion 
    producto.imagen = entrada.imagen
    producto.categorias = entrada.categorias
    producto.subcategorias = entrada.subcategorias
    producto.unidadesDeMedida = entrada.unidadesDeMedida
    producto.precio = entrada.precio
    producto.stock = entrada.stock
    db.commit()
    db.refresh(producto)
    return producto


@router.delete("/eliminar-producto/{productId}",response_model=page_schemas.respuesta)
def del_product(productId: int,db:session=Depends(get_product)):
    producto = db.query(page_models.Productos).filter_by(id=productId).first()
    db.delete(producto)
    db.commit()
    respuesta = page_schemas.respuesta(mensaje="Eliminado exitosamente")
    return respuesta