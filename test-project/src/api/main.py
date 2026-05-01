from fastapi import FastAPI, status

from .models import Post
from .utils import check_index, check_list

app = FastAPI()

list_of_posts = []


@app.get("/posts", status_code=status.HTTP_200_OK)
def get_posts() -> dict:
    return check_list(list_of_posts)


@app.get("/posts/{id}", status_code=status.HTTP_200_OK)
def get_post(id: int) -> dict:
    return {
        "detail": "Post found",
        "post": list_of_posts[check_index(id, list_of_posts)],
    }


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post) -> dict:
    list_of_posts.append(post)
    return {"detail": "Post created", "post": post}


@app.put("/posts/{id}", status_code=status.HTTP_200_OK)
def update_post(id: int, post: Post) -> dict:
    list_of_posts[check_index(id, list_of_posts)] = post
    return {"detail": "Post updated", "post": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int) -> None:
    list_of_posts.pop(check_index(id, list_of_posts))
