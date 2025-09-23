# src/domain/models/course.py

import uuid
from datetime import datetime


class Course:
    """Represents a Course entity."""

    def __init__(self, name: str, description: str = None, capacity: int = 30):
        self.id = uuid.uuid4()
        self.name = name
        self.description = description
        self.capacity = capacity
        self.created_at = datetime.now()
        self.teacher = None
        self.enrolled_students = []  # Holds Student objects

    def capacity_reached(self) -> bool:
        """Check if course has reached maximum capacity."""
        return len(self.enrolled_students) >= self.capacity

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, capacity={self.capacity})>"
