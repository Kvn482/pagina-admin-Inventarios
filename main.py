from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from EndPoints import usuarios 
from EndPoints import productos
from EndPoints import almacen

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuarios.router, tags=["Usuarios"])
app.include_router(productos.router, tags=["Productos"])
app.include_router(almacen.router, tags=["Almacen"])