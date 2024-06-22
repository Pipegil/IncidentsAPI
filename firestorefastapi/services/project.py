from typing import List
from uuid import UUID

from firestorefastapi.dao.project import ProjectDAO
from firestorefastapi.schemas.project import Project, ProjectCreate, ProjectUpdate

project_dao = ProjectDAO()


class ProjectService:
    def create_project(self, project_create: ProjectCreate) -> Project:
        return project_dao.create(project_create)

    def get_project(self, id: UUID) -> Project:
        return project_dao.get(id)

    def list_projects(self) -> List[Project]:
        return project_dao.list()

    def update_project(self, id: UUID, project_update: ProjectUpdate) -> Project:
        return project_dao.update(id, project_update)

    def delete_project(self, id: UUID) -> None:
        return project_dao.delete(id)
