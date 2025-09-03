from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import Response, JSONResponse

# Crée une instance de l'application FastAPI.
app = FastAPI()

# Le modèle Pydantic correspond au schéma Student du fichier YAML.
class Student(BaseModel):
    reference: str
    first_name: str
    last_name: str
    age: int

# Une liste pour stocker nos étudiants.
students_store: List[Student] = []

@app.get('/ping')
def ping():
    return Response(content="pong", status_code=200, media_type="text/plain")

@app.get('/welcome')
def welcome(name: str):
    return Response(content=f"Welcome {name}!", status_code=200, media_type="text/plain")

@app.get('/students')
def get_students():
    return JSONResponse(content=[], status_code=200, media_type="application/json")

@app.post('/students')
def create_students(students_payload: List[Student]):
    global students_store # Permet de modifier la liste students_store
    students_store.extend(students_payload)
    return JSONResponse(content=students_store, status_code=201, media_type="application/json")