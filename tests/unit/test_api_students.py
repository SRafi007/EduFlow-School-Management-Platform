# tests/integration/test_api_students.py
import pytest


@pytest.mark.asyncio
async def test_create_student(client):
    response = await client.post("/students/", params={"name": "Alice", "email": "alice@example.com"})
    data = response.json()
    assert response.status_code == 200
    assert "id" in data
    assert data["name"] == "Alice"
