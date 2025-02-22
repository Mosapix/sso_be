from datetime import datetime
import uuid

from sqlalchemy import Column, Boolean, DateTime, UUID
from sqlalchemy.ext.declarative import  as_declarative

@as_declarative()
class Base:
    id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    updated_at = Column(DateTime(timezone=True), nullable=True)

    __name__: str