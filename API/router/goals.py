from fastapi import APIRouter
from MongoDB.mongo import db
from bson import json_util
from json import loads

router=APIRouter()

@router.get("/goals")
def get_matches():
    res=list(db["Goals"].find({"England":11}))
    print(res)
    return loads(json_util.dumps(res))
