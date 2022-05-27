from fastapi import APIRouter
from MongoDB.mongo import db
from bson import json_util
from json import loads

router=APIRouter()

@router.get("/matches/{stage}")
def get_matches(stage):
    res=list(db["Matches"].find({"stage":stage}))
    print(res)
    return loads(json_util.dumps(res))
