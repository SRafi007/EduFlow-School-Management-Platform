# src/infrastructure/db/init_db.py
from src.infrastructure.db.base import Base
from src.infrastructure.db.session import engine

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
