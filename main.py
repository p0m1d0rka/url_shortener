from fastapi import FastAPI
from pydantic import BaseModel
import redis
import time

db = redis.Redis(host="localhost", port=6379, db=0)

app = FastAPI()

class Shortener(BaseModel):
    full_url: str
    short_url: str
    # created_at: int
    # created_by: str
    # description: str = None

@app.get("/")
async def get_root():
    return {"Hello": "World"}

@app.get("/healthcheck")
async def get_headlthcheck():
    return {"status": "ok"}

@app.get("/shortener/{short_url}")
async def get_full_url(short_url: str, q: str = None):
    return {"full_url": db.get(short_url)}

@app.post("/shortener/")
async def create_shortener(shortener: Shortener):
    db.set(time.time(), shortener.full_url)
    return shortener

