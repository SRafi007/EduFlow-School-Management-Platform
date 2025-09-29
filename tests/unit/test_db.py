# test_db.py
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from src.config.settings import settings

async def main():
    engine = create_async_engine(settings.database_url, echo=False)
    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            print("DB connection OK, SELECT 1 ->", result.scalar())
    finally:
        await engine.dispose()

if __name__ == "__main__":
    asyncio.run(main())
