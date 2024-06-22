from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    email: str
    name: str
    password: int


class UserLogin(BaseModel):
    email: str
    password: int


class UserCreate(UserBase):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fdetal@mail.com",
                "name": "Fulano De Tal",
                "password": 123456,
            }
        }


class UserUpdate(UserBase):
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fdetal@mail.com",
                "name": "Fulano De Tal",
                "password": 0,
            }
        }


class User(UserBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
