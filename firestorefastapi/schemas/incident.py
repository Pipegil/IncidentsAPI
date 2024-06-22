from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class IncidentBase(BaseModel):
    title: str
    description: str
    severity: str
    category_id: str
    project_id: str
    support_id: str
    state: str


class IncidentsStateResponse(BaseModel):
    pending: int
    solved: int
    assigned: int


class IncidentCreate(IncidentBase):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "A Incident",
                "description": "A Incident Description",
                "severity": "M",
                "category_id": "a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p",
                "project_id": "a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p",
                "support_id": "a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p",
                "state": "assigned",
            }
        }


class IncidentUpdate(IncidentBase):
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "A Incident",
                "description": "A Incident Description",
                "severity": "M",
                "category_id": "a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p",
                "project_id": "a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p",
                "support_id": "a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p",
                "state": "assigned",
            }
        }


class Incident(IncidentBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
