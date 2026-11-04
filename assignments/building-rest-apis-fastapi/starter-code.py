from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Books API")


class BookInput(BaseModel):
    title: str
    author: str


class Book(BookInput):
    id: int


books: dict[int, Book] = {}
next_book_id = 1


@app.get("/")
def read_root():
    return {"message": "Books API is running"}