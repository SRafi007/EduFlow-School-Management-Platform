# src/interfaces/api/courses.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.db.session import get_session
from src.application.services.course_service import CourseService
from src.interfaces.schemas.course_schema import CourseCreate, CourseOut

router = APIRouter()

@router.post("/", response_model=CourseOut)
async def create_course(payload: CourseCreate, session: AsyncSession = Depends(get_session)):
    course = await CourseService.create_course(session, payload.name, payload.description, payload.capacity)
    return course

@router.get("/{course_id}", response_model=CourseOut)
async def get_course(course_id: str, session: AsyncSession = Depends(get_session)):
    course = await CourseService.get_course(session, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course
