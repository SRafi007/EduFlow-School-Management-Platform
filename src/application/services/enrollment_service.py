# src/application/services/enrollment_service.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.infrastructure.db.models.enrollment import Enrollment as EnrollmentDB
from src.infrastructure.db.models.student import Student as StudentDB
from src.infrastructure.db.models.course import Course as CourseDB
from src.application.mappers.enrollment_mapper import to_db, to_domain
from src.application.mappers.student_mapper import to_domain as student_to_domain
from src.application.mappers.course_mapper import to_domain as course_to_domain
from src.domain.models.enrollment import Enrollment
from src.utils.exceptions import BusinessRuleViolation


class EnrollmentService:
    @staticmethod
    async def enroll_student(
        session: AsyncSession, student_id, course_id
    ) -> Enrollment:
        # Load student and course
        db_student = await session.get(StudentDB, student_id)
        db_course = await session.get(CourseDB, course_id)

        if not db_student or not db_course:
            raise BusinessRuleViolation("Student or course not found.")

        student = student_to_domain(db_student)
        course = course_to_domain(db_course)

        # Check duplicate enrollment
        stmt = select(EnrollmentDB).where(
            EnrollmentDB.student_id == student_id,
            EnrollmentDB.course_id == course_id,
        )
        result = await session.execute(stmt)
        if result.scalar_one_or_none():
            raise BusinessRuleViolation("Student already enrolled in this course.")

        # Check capacity
        stmt_count = select(EnrollmentDB).where(EnrollmentDB.course_id == course_id)
        result_count = await session.execute(stmt_count)
        enrolled_count = len(result_count.scalars().all())
        if enrolled_count >= course.capacity:
            raise BusinessRuleViolation("Course is already full.")

        # Create enrollment
        enrollment = Enrollment(student, course)
        db_enrollment = to_db(enrollment)
        session.add(db_enrollment)
        await session.commit()
        await session.refresh(db_enrollment)

        return to_domain(db_enrollment, student, course)
