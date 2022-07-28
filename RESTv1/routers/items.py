import os
from fastapi import APIRouter
router = APIRouter()
from typing import Union

from pydantic import BaseModel
class Item(BaseModel):
    name: str
    age: str
    hometown: Union[str, None] = None

# Database Connectivity.
from deta import Deta
key = os.getenv('DETA_KEY')
deta = Deta(key)
db = deta.Base('RESTv1')


@router.post("/items")
def post_item(item: Item):
    user = db.put(dict(item))
    return user

@router.get("/item/{key}")
def read_items(key: Union[str, None] = None):
    #print([d for d in db.fetch()])
    # if key == None:
    #     d = db.fetch()
    # else:
    #     d = db.get(key)

    print(key)
    return ({
        "data" : db.get(key) if key else db.fetch()
    })

# @router.get("/items/{key}")
# def read_item(key: str):
#     #print([d for d in db.fetch()])
#     user = {
#         "data" : db.get(key)
#     }
#     return user

@router.put("/items/{key}")
def update_item(item: Item, key: str):
    print(dict(item))
    user = db.update(dict(item), key)
    return user

@router.delete("/items/{key}")
def update_item(item: Item, key: str):
    print(dict(item))
    user = db.update(dict(item), key)
    return user