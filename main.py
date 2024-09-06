## API - interfaz de programación de aplicaciones
## REST - transferir información . recursos
from typing import List, Optional
import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Inicializar una variable de caracteristicas API REST
app = FastAPI()


# Se define el modelo
class Curso(BaseModel):
    id: Optional[str] = None
    nombre: str
    descripcion: Optional[str] = None
    nivel: str
    duracion: int

# Simular base de datos

cursos_db = []

# CRUD: read (lectura) GET ALL: leer todos los cursos de la base de datos

@app.get("/cursos/", response_model=List[Curso])

def obtenerCursos():
    return cursos_db

# CRUD: Create (escribir) POST: agregar un nuevo recurso a base de datos 

@app.post("/cursos/", response_model=Curso)

def crearCurso(curso:Curso):
    curso.id = str(uuid.uuid4()) #generar un id único
    cursos_db.append(curso)
    return curso

# CRUD read(lectura individual)  GET: leer curso que coincide con id

@app.get("/cursos/{curso_id}", response_model=Curso)

def obtenerCursoInd(curso_id:str):
    curso = next((curso for curso in cursos_db if curso.id == curso_id), None) # next toma la primera coincidencia
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return curso

# CRUD: Update (actualizar) PUT: individual, modificar un recurso que coincida con el ID

@app.put("/cursos/{curso_id}", response_model=Curso)

def actualizarCurso(curso_id:str, curso_actualizado:Curso):
    curso = next((curso for curso in cursos_db if curso.id == curso_id), None) # next toma la primera coincidencia
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    curso_actualizado.id = curso_id
    index = cursos_db.index(curso) #buscar indice del registro
    cursos_db[index] = curso_actualizado
    return curso_actualizado

# CRUD Delete (eliminar) DELETE: Eliminaremos un recurso que coincida con el id qu mandemos 

@app.delete("/cursos/{curso_id}", response_model=Curso)

def eliminarCursoInd(curso_id:str):
    curso = next((curso for curso in cursos_db if curso.id == curso_id), None) # next toma la primera coincidencia
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    cursos_db.remove(curso)
    return curso