# tests/integration/test_api_courses.py
import pytest


@pytest.mark.asyncio
async def test_create_course(client):
    response = await client.post("/courses/", params={"name": "Math 101", "capacity": 2})
    data = response.json()
    assert response.status_code == 200
    assert data["capacity"] == 2
