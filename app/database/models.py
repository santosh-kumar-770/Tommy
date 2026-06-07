from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String, Integer, Text


class Base(DeclarativeBase):
    pass


class Post(Base):

    __tablename__ = "posts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    author = Column(
        String,
        nullable=False
    )
    
    content = Column(
        Text,
        nullable=False
    )

    category = Column(
        String
    )

    importance_score = Column(
        Integer
    )

class Message(Base):

    __tablename__ = "messages"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    person_name = Column(
        String,
        nullable=False
    )

    sender = Column(
        String,
        nullable=False
    )

    message = Column(
        Text,
        nullable=False
    )