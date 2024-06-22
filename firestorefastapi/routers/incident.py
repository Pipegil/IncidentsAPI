from typing import List

from fastapi import APIRouter, Body, HTTPException
from pydantic.types import UUID4

from firestorefastapi.schemas.incident import Incident, IncidentCreate, IncidentUpdate, IncidentsStateResponse
from firestorefastapi.services.incident import IncidentService

router = APIRouter()
incident_service = IncidentService()


@router.post("/incidents", response_model=Incident, tags=["INCIDENTS"])
def create_incident(incident_create: IncidentCreate = Body(...)) -> Incident:
    return incident_service.create_incident(incident_create)


@router.get("/incidents/{id}", response_model=Incident, tags=["INCIDENTS"])
def get_incident(id: UUID4) -> Incident:
    incident = incident_service.get_incident(id)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found.")
    return incident


@router.get("/incidents/state/count", response_model=IncidentsStateResponse, tags=["INCIDENTS"])
def get_incidents_state_count() -> IncidentsStateResponse:
    incident = incident_service.get_incidents_state_count()
    if not incident:
        raise HTTPException(status_code=404, detail="Incident state not found.")
    return incident


@router.get("/incidents", response_model=List[Incident], tags=["INCIDENTS"])
def list_incidents() -> List[Incident]:
    incidents = incident_service.list_incidents()
    if not incidents:
        raise HTTPException(status_code=404, detail="Incidents not found.")
    return incidents


@router.put("/incidents/{id}", response_model=Incident, tags=["INCIDENTS"])
def update_incident(id: UUID4, incident_update: IncidentUpdate = Body(...)) -> Incident:
    incident = incident_service.get_incident(id)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found.")
    return incident_service.update_incident(id, incident_update)


@router.delete("/incidents/{id}", response_model=Incident, tags=["INCIDENTS"])
def delete_incident(id: UUID4) -> Incident:
    incident = incident_service.get_incident(id)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found.")
    return incident_service.delete_incident(id)
