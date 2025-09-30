from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.db.session import get_session
from src.application.services.student_service import StudentService
from src.interfaces.schemas.student_schema import StudentCreate, StudentOut

router = APIRouter()

@router.post("/", response_model=StudentOut)
async def create_student(payload: StudentCreate, session: AsyncSession = Depends(get_session)):
    student = await StudentService.create_student(session, payload.name, payload.email)
    return student

@router.get("/{student_id}", response_model=StudentOut)
async def get_student(student_id: str, session: AsyncSession = Depends(get_session)):
    student = await StudentService.get_student(session, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
