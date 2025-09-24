# src/interfaces/api/students.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.db.session import get_session
from src.application.services.student_service import StudentService

router = APIRouter()

@router.post("/")
async def create_student(name: str, email: str, session: AsyncSession = Depends(get_session)):
    student = await StudentService.create_student(session, name, email)
    return {"id": str(student.id), "name": student.name, "email": student.email}

@router.get("/{student_id}")
async def get_student(student_id: str, session: AsyncSession = Depends(get_session)):
    student = await StudentService.get_student(session, student_id)
    if not student:
        return {"error": "Student not found"}
    return {"id": str(student.id), "name": student.name, "email": student.email}
