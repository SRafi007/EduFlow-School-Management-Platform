# src/domain/models/student.py

from src.domain.models.person import Person


class Student(Person):
    """Represents a Student (Inheritance from Person)."""

    def __init__(self, name: str, email: str):
        super().__init__(name, email)
        self.enrollments = []  # Keeps list of enrolled courses (Encapsulation)

    def role(self) -> str:
        return "Student"

    def enroll(self, course):
        """Enroll student into a course (Polymorphism via method overriding)."""
        if course.capacity_reached():
            raise ValueError(f"Course {course.name} is full.")
        if course in self.enrollments:
            raise ValueError(f"Student already enrolled in {course.name}.")
        self.enrollments.append(course)
        course.enrolled_students.append(self)
