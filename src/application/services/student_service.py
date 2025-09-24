# src/application/services/student_service.py
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.db.models.student import Student as StudentDB
from src.application.mappers.student_mapper import to_db, to_domain
from src.domain.models.student import Student


class StudentService:
    @staticmethod
    async def create_student(session: AsyncSession, name: str, email: str) -> Student:
        domain_student = Student(name, email)
        db_student = to_db(domain_student)
        session.add(db_student)
        await session.commit()
        await session.refresh(db_student)
        return to_domain(db_student)

    @staticmethod
    async def get_student(session: AsyncSession, student_id) -> Student | None:
        db_student = await session.get(StudentDB, student_id)
        return to_domain(db_student) if db_student else None
