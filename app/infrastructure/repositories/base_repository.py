from typing import TypeVar, Generic, List, Optional

from app.infrastructure.database.db_context import get_db_context

T = TypeVar('T')
ID = TypeVar('ID')

class BaseRepository(Generic[T, ID]):
    def __init__(self):
        self.db_context = next(get_db_context())
        self.entity_class = T

    def add(self, entity: T) -> None:
        self.db_context.add(entity)
        self.db_context.commit()

    def get_by_id(self, entity_id: ID) -> Optional[T]:
        return self.db_context.query(self.entity_class).get(entity_id)

    def get_all(self) -> List[T]:
        return self.db_context.query(self.entity_class).all()

    def update(self, entity: T) -> None:
        self.db_context.merge(entity)
        self.db_context.commit()

    def delete(self, entity_id: ID) -> None:
        entity = self.get_by_id(entity_id)
        if entity:
            entity.is_deleted = True
            self.update(entity)
        else:
            raise ValueError(f"Entity with ID {entity_id} does not exist.")