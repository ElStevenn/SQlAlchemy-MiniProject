from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, CheckConstraint, Date, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

import os
cls = lambda: os.system('cls')
engine = create_engine('sqlite:///databases/databases.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# 
from Others import HashGen


"""Relationship databases"""
Book_Author = Table(
    "Author_Book",
    Base.metadata,
    Column("Books_ID", ForeignKey("Books.Books_ID"), primary_key=True),
    Column("Author_id", ForeignKey("Authors.Author_id"), primary_key=True)

)

Book_Genere = Table(
    "Book_Genere",
    Base.metadata,
    Column("Books_ID", ForeignKey("Books.Books_ID"), primary_key=True),
    Column("Genere_ID", ForeignKey("Generes.Genere_ID"), primary_key=True)
)


# Tables

class Authors(Base, HashGen):
    """Author table"""
    __tablename__ = "Authors"

    Author_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    Name = Column(String, nullable=False)
    Birth_date = Column(Date, nullable=False)



class Books(Base, HashGen):
    """Books table"""
    __tablename__ = "Books"

    Books_ID = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    Title = Column(String, nullable=False)
    Publication_Date = Column(Date, nullable=False)


class Generes(Base, HashGen):
    """Generes Table"""
    __tablename__ = "Generes"

    Genere_ID = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    Genere_Name = Column(String, nullable=False)



if __name__ == '__main__':
    Base.metadata.create_all(engine)

    