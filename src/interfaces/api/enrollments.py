# src/interfaces/api/enrollments.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.db.session import get_session
from src.application.services.enrollment_service import EnrollmentService
from src.utils.exceptions import BusinessRuleViolation
from src.interfaces.schemas.enrollment_schema import EnrollmentCreate, EnrollmentOut

router = APIRouter()

@router.post("/", response_model=EnrollmentOut)
async def enroll_student(payload: EnrollmentCreate, session: AsyncSession = Depends(get_session)):
    try:
        enrollment = await EnrollmentService.enroll_student(session, payload.student_id, payload.course_id)
        return {
            "id": enrollment.id,
            "student": enrollment.student.name,
            "course": enrollment.course.name,
        }
    except BusinessRuleViolation as e:
        raise HTTPException(status_code=400, detail=e.message)
