# src/application/mappers/student_mapper.py

from src.domain.models.student import Student
from src.infrastructure.db.models.student import Student as StudentDB


def to_db(domain_student: Student) -> StudentDB:
    """Convert domain Student -> DB Student."""
    return StudentDB(
        id=domain_student.id,
        name=domain_student.name,
        email=domain_student.email,
    )


def to_domain(db_student: StudentDB) -> Student:
    """Convert DB Student -> domain Student."""
    student = Student(name=db_student.name, email=db_student.email)
    student.id = db_student.id  # preserve UUID
    return student
