from typing import List
from uuid import UUID

from firestorefastapi.database import db
from firestorefastapi.schemas.project import Project, ProjectCreate, ProjectUpdate


class ProjectDAO:
    collection_name = "projects"

    def create(self, project_create: ProjectCreate) -> Project:
        data = project_create.dict()
        data["id"] = str(data["id"])
        doc_ref = db.collection(self.collection_name).document(str(project_create.id))
        doc_ref.set(data)
        return self.get(project_create.id)

    def get(self, id: UUID) -> Project:
        doc_ref = db.collection(self.collection_name).document(str(id))
        doc = doc_ref.get()
        if doc.exists:
            return Project(**doc.to_dict())
        return

    def list(self) -> List[Project]:
        projects_ref = db.collection(self.collection_name)
        return [
            Project(**doc.get().to_dict())
            for doc in projects_ref.list_documents()
            if doc.get().to_dict()
        ]

    def update(self, id: UUID, project_update: ProjectUpdate) -> Project:
        data = project_update.dict()
        doc_ref = db.collection(self.collection_name).document(str(id))
        doc_ref.update(data)
        return self.get(id)

    def delete(self, id: UUID) -> None:
        db.collection(self.collection_name).document(str(id)).delete()
