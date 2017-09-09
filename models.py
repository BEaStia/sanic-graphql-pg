from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func, JSON
from sqlalchemy.orm import backref, relationship

from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Entity(Base):
    __tablename__ = 'entities'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    provider = Column(String)
    data = Column(JSON)
    user = relationship(
        User,
        backref=backref(
            'entities',
            uselist=True,
            cascade='delete,all'
        )
    )
