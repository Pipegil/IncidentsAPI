from typing import List

from fastapi import APIRouter, Body, HTTPException
from pydantic.types import UUID4


from firestorefastapi.schemas.project import Project, ProjectCreate, ProjectUpdate
from firestorefastapi.services.project import ProjectService

router = APIRouter()
project_service = ProjectService()


@router.post("/projects", response_model=Project, tags=["PROJECTS"])
def create_project(project_create: ProjectCreate = Body(...)) -> Project:
    return project_service.create_project(project_create)


@router.get("/projects/{id}", response_model=Project, tags=["PROJECTS"])
def get_project(id: UUID4) -> Project:
    project = project_service.get_project(id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found.")
    return project


@router.get("/projects", response_model=List[Project], tags=["PROJECTS"])
def list_projects() -> List[Project]:
    projects = project_service.list_projects()
    if not projects:
        raise HTTPException(status_code=404, detail="Projects not found.")
    return projects


@router.put("/projects/{id}", response_model=Project, tags=["PROJECTS"])
def update_project(id: UUID4, project_update: ProjectUpdate = Body(...)) -> Project:
    project = project_service.get_project(id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found.")
    return project_service.update_project(id, project_update)


@router.delete("/projects/{id}", response_model=Project, tags=["PROJECTS"])
def delete_project(id: UUID4) -> Project:
    project = project_service.get_project(id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found.")
    return project_service.delete_project(id)
