from datetime import datetime

from sqlalchemy import Integer, String, Column, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship

from datebase import Base


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    nameBook = Column(String(20), nullable=False)
    avtor = Column(String(20), nullable=False)
    genre = Column(String(20), nullable=False)
    kindOf = Column(String(40), nullable=False)
    year = Column(Integer, nullable=False)
    code = Column(String(25), nullable=False)


class UserBook(Base):
    __tablename__ = 'userbook'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    surname_name = Column(String(20), nullable=False)
    email = Column(String(40), nullable=False)
    number = Column(String(25), nullable=False)


class PublishedBook(Base):
    __tablename__ = 'publishedbook'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('userbook.id'), nullable=False)
    book_id = Column(Integer, ForeignKey('book.id'), nullable=False)
    dateOfIssue = Column(DateTime, default=datetime.utcnow())
    dateOfReturn = Column(DateTime, default=datetime.utcnow())