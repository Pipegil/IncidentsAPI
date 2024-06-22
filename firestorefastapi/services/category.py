from typing import List
from uuid import UUID

from firestorefastapi.dao.category import CategoryDAO
from firestorefastapi.schemas.category import Category, CategoryCreate, CategoryUpdate


class CategoryService:
    def __init__(self):
        self.category_dao = CategoryDAO()

    def create_category(self, category_create: CategoryCreate) -> Category:
        return self.category_dao.create(category_create)

    def get_category(self, id: UUID) -> Category:
        return self.category_dao.get(id)

    def get_categories_by_project(self, project_id: UUID) -> List[Category]:
        return self.category_dao.get_by_project(project_id)

    def list_categorys(self) -> List[Category]:
        return self.category_dao.list()

    def update_category(self, id: UUID, category_update: CategoryUpdate) -> Category:
        return self.category_dao.update(id, category_update)

    def delete_category(self, id: UUID) -> None:
        return self.category_dao.delete(id)