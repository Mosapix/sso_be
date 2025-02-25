from sqlalchemy import Column, Integer, String, UUID, ForeignKey, Boolean

from app.domain.entities.base import Base


class UserProfile(Base):
    def __init__(self, user_id):
        self.user_id = user_id

    __tablename__ = 'user_profiles'
    cover_image = Column(String, nullable=True)
    profile_image = Column(String, nullable=True)
    gender = Column(Integer, nullable=True)
    user_id = Column(UUID, ForeignKey('users.id'))
    website_url = Column(String, nullable=True)
    about_text = Column(String, nullable=True)
