# src/application/mappers/teacher_mapper.py

from src.domain.models.teacher import Teacher
from src.infrastructure.db.models.teacher import Teacher as TeacherDB


def to_db(domain_teacher: Teacher) -> TeacherDB:
    return TeacherDB(
        id=domain_teacher.id,
        name=domain_teacher.name,
        email=domain_teacher.email,
    )


def to_domain(db_teacher: TeacherDB) -> Teacher:
    teacher = Teacher(name=db_teacher.name, email=db_teacher.email)
    teacher.id = db_teacher.id
    return teacher
