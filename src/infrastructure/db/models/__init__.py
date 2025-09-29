from src.infrastructure.db.base import Base
from src.infrastructure.db.models.scraped_resource import ScrapedResource
from src.infrastructure.db.models.student import Student
from src.infrastructure.db.models.teacher import Teacher
from src.infrastructure.db.models.course import Course
from src.infrastructure.db.models.enrollment import Enrollment

__all__ = ["Base", "ScrapedResource", "Student", "Teacher", "Course", "Enrollment"]
