# src/domain/models/person.py

from abc import ABC, abstractmethod
from datetime import datetime
import uuid


class Person(ABC):
    """Abstract base class for common person attributes (Abstraction)."""

    def __init__(self, name: str, email: str):
        self.id = uuid.uuid4()
        self.name = name
        self.email = email
        self.created_at = datetime.now()

    @abstractmethod
    def role(self) -> str:
        """Each subclass must implement its role."""
        pass

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id}, name={self.name}, email={self.email})>"
