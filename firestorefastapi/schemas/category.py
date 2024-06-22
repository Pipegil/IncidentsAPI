from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    name: str
    project_id: str


class CategoryCreate(CategoryBase):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "A Category",
                "project_id": "a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p",
            }
        }


class CategoryUpdate(CategoryBase):
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "A Category",
                "project_id": "a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p",
            }
        }


class Category(CategoryBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
