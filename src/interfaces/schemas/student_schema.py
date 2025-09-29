from pydantic import BaseModel, EmailStr
from uuid import UUID

class StudentCreate(BaseModel):
    name: str
    email: EmailStr

class StudentOut(BaseModel):
    id: UUID
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
