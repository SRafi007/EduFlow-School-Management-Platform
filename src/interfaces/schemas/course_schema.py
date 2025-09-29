from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class CourseCreate(BaseModel):
    name: str
    description: Optional[str] = None
    capacity: int = 30

class CourseOut(BaseModel):
    id: UUID
    name: str
    description: Optional[str]
    capacity: int

    class Config:
        orm_mode = True
