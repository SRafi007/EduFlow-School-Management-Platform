# src/interfaces/api/enrollments.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.db.session import get_session
from src.application.services.enrollment_service import EnrollmentService
from src.utils.exceptions import BusinessRuleViolation

router = APIRouter()

@router.post("/")
async def enroll_student(student_id: str, course_id: str, session: AsyncSession = Depends(get_session)):
    try:
        enrollment = await EnrollmentService.enroll_student(session, student_id, course_id)
        return {
            "id": str(enrollment.id),
            "student": enrollment.student.name,
            "course": enrollment.course.name,
        }
    except BusinessRuleViolation as e:
        return {"error": e.message}
