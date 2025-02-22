from uuid import UUID

from app.domain.entities.user_profile import UserProfile
from app.infrastructure.repositories.base_repository import BaseRepository

class UserProfileRepository(BaseRepository[UserProfile, UUID]):
    def __init__(self):
        super().__init__()