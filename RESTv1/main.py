from typing import Union
from fastapi import FastAPI, APIRouter
from deta import Deta
from pydantic import BaseModel

import os
from dotenv import load_dotenv
load_dotenv()

key = os.getenv('DETA_KEY')

app = FastAPI()
deta = Deta(key) # configure your Deta project
db = deta.Base('RESTv1')

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

from routers import items, candidate
app.include_router(items.router)
app.include_router(candidate.router)