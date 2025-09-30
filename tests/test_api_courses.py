import pytest
from httpx import AsyncClient
from src.interfaces.api.main import app
from src.infrastructure.db.init__db import init_db

@pytest.fixture(scope="module")
async def client():
    await init_db()
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.mark.asyncio
async def test_create_and_get_course(client):
    payload = {"name": "History 101", "description": "Intro course", "capacity": 2}
    r = await client.post("/courses/", json=payload)
    assert r.status_code == 200
    course_id = r.json()["id"]

    r2 = await client.get(f"/courses/{course_id}")
    assert r2.status_code == 200
    assert r2.json()["name"] == "History 101"
