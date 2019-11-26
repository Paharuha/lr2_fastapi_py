from typing import List

import schemas
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT

import crud
import models
from datebase import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# Book endpoints
@app.get('/api/books/{book_id}', response_model=schemas.Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@app.get('/api/books', response_model=List[schemas.Book])
def get_books(db: Session = Depends(get_db)):
    return crud.get_books(db=db)


@app.post('/api/books', response_model=schemas.Book, status_code=HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)


@app.put('/api/books/{book_id}', response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.update_book(db=db, book_id=book_id, book=book)


@app.delete('/api/books/{book_id}', status_code=HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    crud.delete_book(db=db, book_id=book_id)


# UserBook endpoints
@app.get('/api/userbook/{userbook_id}', response_model=schemas.UserBook)
def get_userbook(userbook_id: int, db: Session = Depends(get_db)):
    db_userbook = crud.get_userbook(db, userbook_id=userbook_id)
    if db_userbook is None:
        raise HTTPException(status_code=404, detail="UserBook not found")
    return db_userbook


@app.get('/api/userbook', response_model=List[schemas.UserBook], response_model_exclude={'password'})
def get_userbook(db: Session = Depends(get_db)):
    return crud.get_userbook(db=db)


@app.post('/api/userbook', response_model=schemas.UserBook, response_model_exclude={'password'},
          status_code=HTTP_201_CREATED)
def create_userbook(userbook: schemas.UserBookCreate, db: Session = Depends(get_db)):
    return crud.create_userbook(db=db, userbook=userbook)


@app.put('/api/userbook/{userbook_id}', response_model=schemas.UserBook)
def update_book(userbook_id: int, userbook: schemas.UserBookCreate, db: Session = Depends(get_db)):
    return crud.update_userbook(db=db, userbook_id=userbook_id, userbook=userbook)


@app.delete('/api/userbook/{userbook_id}', status_code=HTTP_204_NO_CONTENT)
def delete_book(userbook_id: int, db: Session = Depends(get_db)):
    crud.delete_userbook(db=db, userbook_id=userbook_id)


# PublishedBook endpoints
@app.get('/api/publishedbook/{publishedbook_id}', response_model=schemas.PublishedBook)
def get_publishedbook(publishedbook_id: int, db: Session = Depends(get_db)):
    db_publishedbook = crud.get_publishedbook(db, publishedbook_id=publishedbook_id)
    if db_publishedbook is None:
        raise HTTPException(status_code=404, detail="PublishedBook not found")
    return db_publishedbook


@app.get('/api/publishedbook', response_model=List[schemas.PublishedBook])
def get_publishedbook(db: Session = Depends(get_db)):
    return crud.get_publishedbook(db=db)


@app.post('/api/publishedbook', response_model=schemas.PublishedBook, status_code=HTTP_201_CREATED)
def create_publishedbook(publishedbook: schemas.PublishedBookCreate, db: Session = Depends(get_db)):
    return crud.create_publishedbook(db=db, publishedbook=publishedbook)


@app.put('/api/publishedbook/{publishedbook_id}', response_model=schemas.PublishedBook)
def update_book(publishedbook_id: int, publishedbook: schemas.PublishedBookCreate, db: Session = Depends(get_db)):
    return crud.update_publishedbook(db=db, publishedbook_id=publishedbook_id, publishedbook=publishedbook)


@app.delete('/api/publishedbook/{publishedbook_id}', status_code=HTTP_204_NO_CONTENT)
def delete_book(publishedbook_id: int, db: Session = Depends(get_db)):
    crud.delete_publishedbook(db=db, publishedbook_id=publishedbook_id)
