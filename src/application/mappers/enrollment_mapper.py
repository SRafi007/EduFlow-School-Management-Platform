# src/application/mappers/enrollment_mapper.py

from src.domain.models.enrollment import Enrollment
from src.infrastructure.db.models.enrollment import Enrollment as EnrollmentDB


def to_db(domain_enrollment: Enrollment) -> EnrollmentDB:
    return EnrollmentDB(
        id=domain_enrollment.id,
        student_id=domain_enrollment.student.id,
        course_id=domain_enrollment.course.id,
    )


def to_domain(db_enrollment: EnrollmentDB, student, course) -> Enrollment:
    enrollment = Enrollment(student=student, course=course)
    enrollment.id = db_enrollment.id
    return enrollment
