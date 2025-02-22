from typing import Optional
from uuid import UUID

from app.infrastructure.repositories.base_repository import BaseRepository
from app.domain.entities.user import User


class UserRepository(BaseRepository[User, UUID]):
    def __init__(self):
        super().__init__()

    def get_by_email(self, email: str) -> Optional[User]:
        return self.db_context.query(User).filter(User.email == email).first()
