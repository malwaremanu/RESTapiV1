import os
from fastapi import APIRouter
router = APIRouter()
from typing import Union

from pydantic import BaseModel
class Candidate(BaseModel):
    roll_no: int
    reg_no: int
    name : str
    email: str

class Candidate_login(BaseModel):
    roll_no: int
    reg_no: int

# Database Connectivity.
from deta import Deta
key = os.getenv('DETA_KEY')
deta = Deta(key)
db = deta.Base('RESTv1-Candidate')

@router.post("/login")
def login_candidate(login_info: Candidate_login):
    print(dict(login_info))
    a = db.fetch({
        "roll_no" : dict(login_info).get("roll_no"),
        "reg_no" : dict(login_info).get("reg_no")
    })
    return ({
        #"data" : db.get(key) if key else db.fetch()
        "msg" : "success",
        "a" : a
    })

@router.get("/candidates")
def read_candidates():
    return ({
        "data" : db.fetch()
    })

@router.post("/candidates")
def post_candidate(candidate: Candidate):
    user = db.put(dict(candidate))
    return user

@router.get("/candidates/{key}")
def read_candidate(key: Union[str, None] = None):
    return ({
        "data" : db.get(key) if key else db.fetch()
    })

@router.put("/candidates/{key}")
def update_candidate(candidate: Candidate, key: str):
    print(dict(candidate))
    user = db.update(dict(candidate), key)
    return db.get(key)

@router.delete("/candidates/{key}")
def update_candidate(candidate: Candidate, key: str):
    print(dict(candidate))
    user = db.update(dict(candidate), key)
    return ({
        "msg" : "Deleted"
    })