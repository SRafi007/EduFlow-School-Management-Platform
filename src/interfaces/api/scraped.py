# src/interfaces/api/scraped.py

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.infrastructure.db.session import get_session
from src.infrastructure.db.models.scraped_resource import ScrapedResource

router = APIRouter()


@router.get("/")
async def list_scraped_resources(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(ScrapedResource))
    resources = result.scalars().all()
    return [
        {
            "id": str(r.id),
            "title": r.title,
            "author": r.author,
            "source_url": r.source_url,
            "content": r.content,
        }
        for r in resources
    ]
