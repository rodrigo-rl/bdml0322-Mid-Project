import requests
import pandas as pd


def players(country):
    
    aux=requests.get(f"https://api-midproj.herokuapp.com/players/{country}").json()
 
    return aux

def goals():
    
    aux=requests.get("https://api-midproj.herokuapp.com/goals/").json()
 
    return aux


def teams(team):    
    aux=requests.get(f"https://api-midproj.herokuapp.com/teams/{team}").json()

    return aux