# tests/integration/test_api_enrollments.py
import pytest


@pytest.mark.asyncio
async def test_enroll_student(client):
    # Create student
    s_res = await client.post("/students/", params={"name": "Bob", "email": "bob@example.com"})
    student_id = s_res.json()["id"]

    # Create course
    c_res = await client.post("/courses/", params={"name": "Physics 101", "capacity": 1})
    course_id = c_res.json()["id"]

    # Enroll
    e_res = await client.post("/enrollments/", params={"student_id": student_id, "course_id": course_id})
    data = e_res.json()

    assert e_res.status_code == 200
    assert data["student"] == "Bob"
    assert data["course"] == "Physics 101"
