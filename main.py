from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

@app.get("/")
def root():
    return {"message": "It's works."}

@app.get("/posts")
def get_posts():
    return {"data": "This is a test post."}

@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post)
    return {"data": "new_post"}


@app.post("/createpost")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title: {payload['title']} content: {payload['content']}"}

