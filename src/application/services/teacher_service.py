# src/application/services/teacher_service.py
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.db.models.teacher import Teacher as TeacherDB
from src.application.mappers.teacher_mapper import to_db, to_domain
from src.domain.models.teacher import Teacher


class TeacherService:
    @staticmethod
    async def create_teacher(session: AsyncSession, name: str, email: str) -> Teacher:
        domain_teacher = Teacher(name, email)
        db_teacher = to_db(domain_teacher)
        session.add(db_teacher)
        await session.commit()
        await session.refresh(db_teacher)
        return to_domain(db_teacher)

    @staticmethod
    async def get_teacher(session: AsyncSession, teacher_id) -> Teacher | None:
        db_teacher = await session.get(TeacherDB, teacher_id)
        return to_domain(db_teacher) if db_teacher else None
