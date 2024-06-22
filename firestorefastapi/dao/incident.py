from typing import List
from uuid import UUID

from google.cloud.firestore_v1 import FieldFilter

from firestorefastapi.database import db
from firestorefastapi.schemas.incident import Incident, IncidentCreate, IncidentUpdate, IncidentsStateResponse


class IncidentDAO:
    collection_name = "incidents"

    def create(self, incident_create: IncidentCreate) -> Incident:
        data = incident_create.dict()
        data["id"] = str(data["id"])
        doc_ref = db.collection(self.collection_name).document(str(incident_create.id))
        doc_ref.set(data)
        return self.get(incident_create.id)

    def get(self, id: UUID) -> Incident:
        doc_ref = db.collection(self.collection_name).document(str(id))
        doc = doc_ref.get()
        if doc.exists:
            return Incident(**doc.to_dict())
        return

    def get_state_count(self) -> IncidentsStateResponse:
        incidents_ref = db.collection(self.collection_name)
        pending = len([doc for doc in incidents_ref.where(filter=FieldFilter('state', '==', 'pending')).stream()])
        solved = len([doc for doc in incidents_ref.where(filter=FieldFilter('state', '==', 'solved')).stream()])
        assigned = len([doc for doc in incidents_ref.where(filter=FieldFilter('state', '==', 'assigned')).stream()])
        return IncidentsStateResponse(pending=pending, solved=solved, assigned=assigned)

    def list(self) -> List[Incident]:
        incidents_ref = db.collection(self.collection_name)
        return [
            Incident(**doc.get().to_dict())
            for doc in incidents_ref.list_documents()
            if doc.get().to_dict()
        ]

    def update(self, id: UUID, incident_update: IncidentUpdate) -> Incident:
        data = incident_update.dict()
        doc_ref = db.collection(self.collection_name).document(str(id))
        doc_ref.update(data)
        return self.get(id)

    def delete(self, id: UUID) -> None:
        db.collection(self.collection_name).document(str(id)).delete()
