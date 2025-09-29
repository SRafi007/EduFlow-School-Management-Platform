from pydantic import BaseModel
from uuid import UUID

class EnrollmentCreate(BaseModel):
    student_id: UUID
    course_id: UUID

class EnrollmentOut(BaseModel):
    id: UUID
    student: str
    course: str

    class Config:
        orm_mode = True
