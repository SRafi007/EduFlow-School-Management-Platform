# src/domain/models/enrollment.py

import uuid
from datetime import datetime


class Enrollment:
    """Represents the association between Student and Course."""

    def __init__(self, student, course):
        self.id = uuid.uuid4()
        self.student = student
        self.course = course
        self.enrolled_at = datetime.now()

    def __repr__(self):
        return f"<Enrollment(student={self.student.name}, course={self.course.name})>"
