# src/interfaces/api/teachers.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.db.session import get_session
from src.application.services.teacher_service import TeacherService

router = APIRouter()

@router.post("/")
async def create_teacher(name: str, email: str, session: AsyncSession = Depends(get_session)):
    teacher = await TeacherService.create_teacher(session, name, email)
    return {"id": str(teacher.id), "name": teacher.name, "email": teacher.email}

@router.get("/{teacher_id}")
async def get_teacher(teacher_id: str, session: AsyncSession = Depends(get_session)):
    teacher = await TeacherService.get_teacher(session, teacher_id)
    if not teacher:
        return {"error": "Teacher not found"}
    return {"id": str(teacher.id), "name": teacher.name, "email": teacher.email}
