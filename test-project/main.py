from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    author: str

list_of_posts = []

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"posts": list_of_posts}

@app.get("/posts/{id}")
def get_post(id: int):
    return {"post_id": list_of_posts[id]}

@app.post("/posts")
def create_post(post: Post):
    list_of_posts.append(post)
    return {"message": "Post created successfully", "posts": list_of_posts}

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    list_of_posts[id] = post
    return {"message": "Post updated successfully", "post_modified": list_of_posts[id]}

@app.delete("/posts/{id}")
def delete_post(id: int):
    list_of_posts.pop(id)
    return {"message": "Post deleted successfully", "posts" : list_of_posts}