# src/application/services/course_service.py
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.db.models.course import Course as CourseDB
from src.application.mappers.course_mapper import to_db, to_domain
from src.domain.models.course import Course


class CourseService:
    @staticmethod
    async def create_course(session: AsyncSession, name: str, description: str = None, capacity: int = 30) -> Course:
        domain_course = Course(name, description, capacity)
        db_course = to_db(domain_course)
        session.add(db_course)
        await session.commit()
        await session.refresh(db_course)
        return to_domain(db_course)

    @staticmethod
    async def get_course(session: AsyncSession, course_id) -> Course | None:
        db_course = await session.get(CourseDB, course_id)
        return to_domain(db_course) if db_course else None
