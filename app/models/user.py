from app.models.base_model import BaseModel, Base
from flask_login import UserMixin
from app import login
from sqlalchemy import Column, Integer, String, BLOB, ForeignKey, LargeBinary, Text
from sqlalchemy.dialects.mysql import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash


class User(BaseModel, UserMixin, Base):
    """Representation of a manpower"""
    __tablename__ = 'users'
    username = Column(String(64), index=True, unique=True)
    email = Column(String(128), index=True, unique=True)
    password_hash = Column(Text)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        # self.password_hash = generate_password_hash(password)
        self.password_hash = password

    def check_password(self, password):
        # return check_password_hash(self.password_hash, password)
        return (self.password_hash == password)

@login.user_loader
def load_user(id):
    from app.models import storage
    user = storage.load_user_by_id(User, id)
    return user
