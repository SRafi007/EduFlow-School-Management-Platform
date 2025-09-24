# tests/conftest.py
import asyncio
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy_utils import create_database, drop_database
from src.infrastructure.db.session import engine, AsyncSessionLocal
from src.infrastructure.db.base import Base
from src.interfaces.api.main import app


TEST_DATABASE_URL = "postgresql+asyncpg://eduflow:dev_password@localhost:5432/eduflow_test"


@pytest.fixture(scope="session")
def event_loop():
    """Create a new event loop for async tests."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
async def setup_test_db():
    """Create a fresh test DB schema."""
    try:
        create_database(TEST_DATABASE_URL)
    except Exception:
        drop_database(TEST_DATABASE_URL)
        create_database(TEST_DATABASE_URL)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()
    drop_database(TEST_DATABASE_URL)


@pytest.fixture
async def db_session():
    async with AsyncSessionLocal() as session:
        yield session


@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
