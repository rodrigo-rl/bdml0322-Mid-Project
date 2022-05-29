from fastapi import APIRouter
from fastapi import APIRouter
from MongoDB.mongo import db
from bson import json_util
from json import loads

router=APIRouter()

@router.get("/players/{country}")
def get_players(country):
    res=list(db["Players"].find({"country":country}))
    print(res)
    return loads(json_util.dumps(res))
