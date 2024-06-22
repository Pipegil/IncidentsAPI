from typing import List

from fastapi import APIRouter, Body, HTTPException
from pydantic.types import UUID4

from firestorefastapi.schemas.category import Category, CategoryCreate, CategoryUpdate
from firestorefastapi.services.category import CategoryService

router = APIRouter()
category_service = CategoryService()


@router.post("/categories", response_model=Category, tags=["CATEGORIES"])
def create_category(category_create: CategoryCreate = Body(...)) -> Category:
    return category_service.create_category(category_create)


@router.get("/categories/{id}", response_model=Category, tags=["CATEGORIES"])
def get_category(id: UUID4) -> Category:
    category = category_service.get_category(id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found.")
    return category


@router.get("/project/categories", response_model=List[Category], tags=["CATEGORIES"])
def get_categories_by_project(project_id: UUID4) -> List[Category]:
    categories = category_service.get_categories_by_project(project_id)
    if not categories:
        raise HTTPException(status_code=404, detail="Categories not found.")
    return categories


@router.get("/categories", response_model=List[Category], tags=["CATEGORIES"])
def list_categories() -> List[Category]:
    categories = category_service.list_categories()
    if not categories:
        raise HTTPException(status_code=404, detail="Categorys not found.")
    return categories


@router.put("/categories/{id}", response_model=Category, tags=["CATEGORIES"])
def update_category(id: UUID4, category_update: CategoryUpdate = Body(...)) -> Category:
    category = category_service.get_category(id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found.")
    return category_service.update_category(id, category_update)


@router.delete("/categories/{id}", response_model=Category, tags=["CATEGORIES"])
def delete_category(id: UUID4) -> Category:
    category = category_service.get_category(id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found.")
    return category_service.delete_category(id)
