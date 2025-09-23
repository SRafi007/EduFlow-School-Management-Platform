# src/domain/models/teacher.py

from src.domain.models.person import Person


class Teacher(Person):
    """Represents a Teacher (Inheritance from Person)."""

    def __init__(self, name: str, email: str):
        super().__init__(name, email)
        self.courses = []

    def role(self) -> str:
        return "Teacher"

    def assign_course(self, course):
        """Assign this teacher to a course."""
        self.courses.append(course)
        course.teacher = self
