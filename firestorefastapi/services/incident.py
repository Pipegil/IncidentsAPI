from typing import List
from uuid import UUID

from firestorefastapi.dao.incident import IncidentDAO
from firestorefastapi.schemas.incident import Incident, IncidentCreate, IncidentUpdate, IncidentsStateResponse

incident_dao = IncidentDAO()


class IncidentService:
    def create_incident(self, incident_create: IncidentCreate) -> Incident:
        return incident_dao.create(incident_create)

    def get_incident(self, id: UUID) -> Incident:
        return incident_dao.get(id)

    def get_incidents_state_count(self) -> IncidentsStateResponse:
        return incident_dao.get_state_count()

    def list_incidents(self) -> List[Incident]:
        return incident_dao.list()

    def update_incident(self, id: UUID, incident_update: IncidentUpdate) -> Incident:
        return incident_dao.update(id, incident_update)

    def delete_incident(self, id: UUID) -> None:
        return incident_dao.delete(id)
