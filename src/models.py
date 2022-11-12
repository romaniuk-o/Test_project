from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from src import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hash = db.Column(db.String(255), nullable=False)
    token_cookie = db.Column(db.String(255), nullable=True, default=None)
    #pictures = relationship('Picture', back_populates='user')

    def __repr__(self):
        return f"User({self.id}, {self.username}, {self.email})"


class Notate(db.Model):
    __tablename__ = 'notates'
    id = db.Column(db.Integer, primary_key=True)
    notate = db.Column(db.String(1000), nullable=False)
    tag = db.Column(db.String(100), nullable=True)

    def __repr__(self):
         return f"User({self.id}, {self.notate}, {self.tag})"

