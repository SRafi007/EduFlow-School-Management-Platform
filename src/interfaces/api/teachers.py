# src/interfaces/api/teachers.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.db.session import get_session
from src.application.services.teacher_service import TeacherService
from src.interfaces.schemas.teacher_schema import TeacherCreate, TeacherOut

router = APIRouter()

@router.post("/", response_model=TeacherOut)
async def create_teacher(payload: TeacherCreate, session: AsyncSession = Depends(get_session)):
    teacher = await TeacherService.create_teacher(session, payload.name, payload.email)
    return teacher

@router.get("/{teacher_id}", response_model=TeacherOut)
async def get_teacher(teacher_id: str, session: AsyncSession = Depends(get_session)):
    teacher = await TeacherService.get_teacher(session, teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

