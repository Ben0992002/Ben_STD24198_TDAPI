from fastapi import FastAPI
from starlette.responses import Response

# Créons une instance de l'application FastAPI, qui est le point de départ.
app = FastAPI()

# Le décorateur @app.get('/ping') indique à FastAPI que la fonction 'ping' doit
# être exécutée lorsque le serveur reçoit une requête HTTP de type GET sur le chemin '/ping'.
@app.get('/ping')
def ping():
    # La fonction retourne un objet Response avec le contenu "pong", le code 200 (OK), et le type de média text/plain.
    return Response(content="pong", status_code=200, media_type="text/plain")