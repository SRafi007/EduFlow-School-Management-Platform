# src/infrastructure/db/models/scraped_resource.py
import uuid
from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from src.infrastructure.db.base import Base


class ScrapedResource(Base):
    __tablename__ = "scraped_resources"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(200), nullable=False)
    author = Column(String(120), nullable=True)
    source_url = Column(String(255), nullable=False)
    content = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
