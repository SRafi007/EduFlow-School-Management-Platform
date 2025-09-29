# src/interfaces/api/scraped.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel
from typing import List
from uuid import UUID  # ✅ import UUID
from src.infrastructure.db.session import get_session
from src.infrastructure.db.models.scraped_resource import ScrapedResource

router = APIRouter()


class ScrapedResourceOut(BaseModel):
    id: UUID   # ✅ UUID instead of str
    title: str
    author: str | None
    source_url: str
    content: str | None

    class Config:
        from_attributes = True   # ✅ Pydantic V2 replacement for orm_mode


@router.get("/", response_model=List[ScrapedResourceOut])
async def list_scraped_resources(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(ScrapedResource))
    return result.scalars().all()
