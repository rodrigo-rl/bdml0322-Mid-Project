from fastapi import APIRouter
from MongoDB.mongo import db
from bson import json_util
from json import loads

router=APIRouter()

@router.get("/teams/{country}")
def get_matches(country):
    res=list(db["Teams"].find({"country":country}))
    print(res)
    return loads(json_util.dumps(res))
