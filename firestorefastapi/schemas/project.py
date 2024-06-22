from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ProjectBase(BaseModel):
    name: str


class ProjectCreate(ProjectBase):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "A Project",
            }
        }


class ProjectUpdate(ProjectBase):
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "A Project",
            }
        }


class Project(ProjectBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
