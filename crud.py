from sqlalchemy.orm import Session
import models
import schemas


# Book CRUD
def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_books(db: Session):
    return db.query(models.Book).all()


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(nameBook=book.nameBook, avtor=book.avtor, genre=book.genre,
                    kindOf=book.kindOf, year=book.year, code=book.code)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def update_book(db: Session, book: schemas.BookCreate, book_id: int):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).nameBook()
    db_book.nameBook = book.nameBook
    db_book.avtor = book.avtor
    db_book.genre = book.genre
    db_book.kindOf = book.kindOf
    db_book.year = book.year
    db_book.code = book.code
    db.commit()
    return db_book


def delete_book(db: Session, book_id: int):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    db.delete(db_book)
    db.commit()


# UserBook CRUD
def get_userbook(db: Session, userbook_id: int):
    return db.query(models.Userbook).filter(models.Userbook.id == userbook_id).first()


def get_userbooks(db: Session):
    return db.query(models.Userbook).all()


def create_userbook(db: Session, userbook: schemas.UserBookCreate):
    db_userbook = models.Userbook(first_name=userbook.first_name, last_name=userbook.last_name, surname_name=userbook.surname_name,
                        email=userbook.email, number=userbook.number)
    db.add(db_userbook)
    db.commit()
    db.refresh(db_userbook)
    return db_userbook


def update_userbook(db: Session, userbook: schemas.UserBookCreate, userbook_id: int):
    db_userbook = db.query(models.Userbook).filter(models.Userbook.id == userbook_id).first()
    db_userbook.first_name = userbook.first_name
    db_userbook.last_name = userbook.last_name
    db_userbook.surname_name = userbook.surname_name
    db_userbook.email = userbook.email
    db_userbook.number = userbook.number
    db.commit()
    return db_userbook


def delete_userbook(db: Session, userbook_id: int):
    db_userbook = db.query(models.Userbook).filter(models.Userbook.id == userbook_id).first()
    db.delete(db_userbook)
    db.commit()


# PublishedBook CRUD
def get_publishedbook(db: Session, publishedbook_id: int):
    return db.query(models.PublishedBook).filter(models.PublishedBook.id == publishedbook_id).first()


def get_publishedbooks(db: Session):
    return db.query(models.PublishedBook).all()


def create_publishedbook(db: Session, publishedbook: schemas.PublishedBookCreate):
    db_publishedbook = models.PublishedBook(user_id=publishedbook.user_id, book_id=publishedbook.book_id,
                                            dateOfIssue=publishedbook.dateOfIssue, dateOfReturn=publishedbook.dateOfReturn)
    db.add(db_publishedbook)
    db.commit()
    db.refresh(db_publishedbook)
    return db_publishedbook


def update_publishedbook(db: Session, publishedbook: schemas.PublishedBookCreate, publishedbook_id: int):
    db_publishedbook = db.query(models.PublishedBook).filter(models.PublishedBook.id == publishedbook_id).first()
    db_publishedbook.user_id = publishedbook.user_id
    db_publishedbook.book_id = publishedbook.book_id
    db_publishedbook.dateOfIssue = publishedbook.dateOfIssue
    db_publishedbook.dateOfReturn = publishedbook.dateOfReturn
    db.commit()
    return db_publishedbook


def delete_publishedbook(db: Session, publishedbook_id: int):
    db_publishedbook = db.query(models.PublishedBook).filter(models.PublishedBook.id == publishedbook_id).first()
    db.delete(db_publishedbook)
    db.commit()