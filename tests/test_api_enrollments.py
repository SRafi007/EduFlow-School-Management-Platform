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
async def test_enrollment_duplicate_and_capacity(client):
    # Create student + course with capacity=1
    s = await client.post("/students/", json={"name": "Alice", "email": "alice@test.com"})
    student_id = s.json()["id"]

    c = await client.post("/courses/", json={"name": "Math 101", "capacity": 1})
    course_id = c.json()["id"]

    # First enrollment should succeed
    e1 = await client.post("/enrollments/", json={"student_id": student_id, "course_id": course_id})
    assert e1.status_code == 200

    # Second enrollment (same student, same course) should fail
    e2 = await client.post("/enrollments/", json={"student_id": student_id, "course_id": course_id})
    assert e2.status_code == 400
    assert "already enrolled" in e2.text

    # Second student should hit capacity rule
    s2 = await client.post("/students/", json={"name": "Bob", "email": "bob@test.com"})
    student2_id = s2.json()["id"]

    e3 = await client.post("/enrollments/", json={"student_id": student2_id, "course_id": course_id})
    assert e3.status_code == 400
    assert "Course is already full" in e3.text
