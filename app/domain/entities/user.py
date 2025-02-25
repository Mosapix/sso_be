from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.domain.entities.base import Base


class User(Base):
    def __init__(self, username, email, hashed_password):
        self.username = username
        self.email = email
        self.hashed_password = hashed_password

    __tablename__ = 'users'
    email = Column(String, unique=True, index=True)
    username = Column(String, index=True)
    display_name = Column(String)
    hashed_password = Column(String)

    user_profile = relationship('UserProfile', uselist=False, backref='user')