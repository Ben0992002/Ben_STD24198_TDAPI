from fastapi import FastAPI
from starlette.responses import Response, JSONResponse

# Crée une instance de l'application FastAPI.
app = FastAPI()


@app.get('/ping')
def ping():
    return Response(content="pong", status_code=200, media_type="text/plain")


@app.get('/welcome')
def welcome(name: str):
    return Response(content=f"Welcome {name}!", status_code=200, media_type="text/plain")


@app.get('/students')
def get_students():
    return JSONResponse(content=[], status_code=200, media_type="application/json")