from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BookBase(BaseModel):
    nameBook: str
    avtor: str
    genre: str
    kindOf: str
    year: int
    code: str


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True


class UserBookBase(BaseModel):
    first_name: str
    last_name: str
    surname_name: str
    email: str
    number: str


class UserBookCreate(UserBookBase):
    pass


class UserBook(UserBookBase):
    id: int

    class Config:
        orm_mode = True


class PublishedBookBase(BaseModel):
    user_id: int
    book_id: int
    dateOfIssue: datetime = None
    dateOfReturn: datetime = None


class PublishedBookCreate(PublishedBookBase):
    pass


class PublishedBook(PublishedBookBase):
    id: int
    userbook: Optional[UserBook]
    book: Optional[Book]

    class Config:
        orm_mode = True
