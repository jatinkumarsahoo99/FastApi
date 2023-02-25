from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title:str
    content:str
    published:bool = True
    rating: Optional[int] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/createposts")
def create_posts(payload : dict =  Body (...)):
    print(payload)
    return {"message": "Hello from post"}

@app.post("/createpost")
def create_posts1(new_post:Post):
    print(new_post.dict())
    return {"message": "Hello from post"}


