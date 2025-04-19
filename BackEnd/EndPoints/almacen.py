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


def get_almacen():
    try:
        db = sessionlocal()
        yield db
    finally:
        db.close()

@router.get("/register-almacen")
async def Main():
    return RedirectResponse(url="/docs/")

@router.get("/ver-almacen/", response_model=List[page_schemas.Almacen])
async def show_almacen(db:session=Depends(get_almacen)):
    almacen = db.query(page_models.Almacen).all()
    return almacen


@router.post("/registrar-almacen/",response_model=page_schemas.Almacen)
def create_user(entrada:page_schemas.Almacen,db:session=Depends(get_almacen)):
   almacen = page_models.Almacen(codigo = entrada.codigo,
                                 nombre = entrada.nombre, 
                                 direccion = entrada.direccion, 
                                 capacidad = entrada.capacidad, 
                                 tipo = entrada.tipo, 
                                 responsable = entrada.responsable)
   db.add(almacen)
   db.commit()
   db.refresh(almacen)
   return almacen

@router.put("/cambiar-almacen/{almacen_id}",response_model=page_schemas.Almacen)
def mod_almacen(almacenId: int, entrada:page_schemas.Almacen,db:session=Depends(get_almacen)):
    almacen = db.query(page_models.Almacen).filter_by(id=almacenId).first()
    almacen.codigo = entrada.codigo
    almacen.nombre = entrada.nombre
    almacen.direccion = entrada.direccion
    almacen.capacidad = entrada.capacidad 
    almacen.tipo = entrada.tipo 
    almacen.responsable = entrada.responsable
    db.commit()
    db.refresh(almacen)
    return almacen


@router.delete("/eliminar-almacen/{almacenId}",response_model=page_schemas.respuesta)
def del_almacen(almacenId: int,db:session=Depends(get_almacen)):
    almacen = db.query(page_models.Almacen).filter_by(id=almacenId).first()
    db.delete(almacen)
    db.commit()
    respuesta = page_schemas.respuesta(mensaje="Eliminado exitosamente")
    return respuesta