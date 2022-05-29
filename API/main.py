from fastapi import FastAPI
from router import partidos, players, equipos,goals

app=FastAPI()
app.include_router(partidos.router)
app.include_router(players.router)
app.include_router(equipos.router)
app.include_router(goals.router)

@app.get("/")
def raiz():
    return {"message":"Bienvenido a mi api"}

@app.get("/one")
def raiz():
    return {"message":"Bienvenido a mi segunda parte"}