# src/interfaces/api/courses.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.db.session import get_session
from src.application.services.course_service import CourseService

router = APIRouter()

@router.post("/")
async def create_course(name: str, description: str = None, capacity: int = 30, session: AsyncSession = Depends(get_session)):
    course = await CourseService.create_course(session, name, description, capacity)
    return {"id": str(course.id), "name": course.name, "capacity": course.capacity}

@router.get("/{course_id}")
async def get_course(course_id: str, session: AsyncSession = Depends(get_session)):
    course = await CourseService.get_course(session, course_id)
    if not course:
        return {"error": "Course not found"}
    return {"id": str(course.id), "name": course.name, "capacity": course.capacity}
