import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, declared_attr

class Base(DeclarativeBase):
    pass

class BaseModelMixin:
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    deleted_at = Column(DateTime(timezone=True), nullable=True, index=True)

class TenantMixin:
    @declared_attr
    def entreprise_id(cls):
        from sqlalchemy import ForeignKey
        return Column(UUID(as_uuid=True), ForeignKey("entreprises.id", ondelete="RESTRICT"), nullable=False, index=True)
    