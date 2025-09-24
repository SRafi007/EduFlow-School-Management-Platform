# src/application/mappers/course_mapper.py

from src.domain.models.course import Course
from src.infrastructure.db.models.course import Course as CourseDB


def to_db(domain_course: Course) -> CourseDB:
    return CourseDB(
        id=domain_course.id,
        name=domain_course.name,
        description=domain_course.description,
        capacity=domain_course.capacity,
        teacher_id=domain_course.teacher.id if domain_course.teacher else None,
    )


def to_domain(db_course: CourseDB) -> Course:
    course = Course(
        name=db_course.name,
        description=db_course.description,
        capacity=db_course.capacity,
    )
    course.id = db_course.id
    return course
