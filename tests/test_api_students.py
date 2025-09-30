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
async def test_create_and_get_student(client):
    payload = {"name": "Charlie", "email": "charlie@test.com"}
    r = await client.post("/students/", json=payload)
    assert r.status_code == 200
    student_id = r.json()["id"]

    r2 = await client.get(f"/students/{student_id}")
    assert r2.status_code == 200
    assert r2.json()["email"] == "charlie@test.com"
