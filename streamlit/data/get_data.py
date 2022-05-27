import requests
import pandas as pd


def get_goles():
    goles=[]
    
    aux=requests.get("https://api-midprojec.herokuapp.com/goles").json()
    for i in aux:#range(len(aux)):
        goles.append(i)

    goals=goles[0]


    return goals
