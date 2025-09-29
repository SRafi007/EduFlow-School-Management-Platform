from pydantic import BaseModel, EmailStr
from uuid import UUID

class TeacherCreate(BaseModel):
    name: str
    email: EmailStr

class TeacherOut(BaseModel):
    id: UUID
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
