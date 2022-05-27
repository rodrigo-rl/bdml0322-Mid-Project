from fastapi import FastAPI
from router import partidos, goles

app=FastAPI()
app.include_router(partidos.router)
app.include_router(goles.router)

@app.get("/")
def raiz():
    return {"message":"Bienvenido a mi api"}

@app.get("/one")
def raiz():
    return {"message":"Bienvenido a mi segunda parte"}