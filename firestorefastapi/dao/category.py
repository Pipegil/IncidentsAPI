from typing import List
from uuid import UUID

from firestorefastapi.database import db
from firestorefastapi.schemas.category import Category, CategoryCreate, CategoryUpdate


class CategoryDAO:
    collection_name = "categories"

    def create(self, category_create: CategoryCreate) -> Category:
        data = category_create.dict()
        data["id"] = str(data["id"])
        data["project_id"] = str(data["project_id"])  # ensure project_id is included
        doc_ref = db.collection(self.collection_name).document(str(category_create.id))
        doc_ref.set(data)
        return self.get(category_create.id)

    def get(self, id: UUID) -> Category:
        doc_ref = db.collection(self.collection_name).document(str(id))
        doc = doc_ref.get()
        if doc.exists:
            return Category(**doc.to_dict())
        return

    def get_by_project(self, project_id: UUID) -> List[Category]:
        categories_ref = db.collection(self.collection_name)
        return [
            Category(**doc.get().to_dict())
            for doc in categories_ref.list_documents()
            if doc.get().to_dict() and doc.get().to_dict().get('project_id') == str(project_id)
        ]

    def list(self) -> List[Category]:
        categories_ref = db.collection(self.collection_name)
        return [
            Category(**doc.get().to_dict())
            for doc in categories_ref.list_documents()
            if doc.get().to_dict()
        ]

    def update(self, id: UUID, category_update: CategoryUpdate) -> Category:
        data = category_update.dict()
        doc_ref = db.collection(self.collection_name).document(str(id))
        doc_ref.update(data)
        return self.get(id)

    def delete(self, id: UUID) -> None:
        db.collection(self.collection_name).document(str(id)).delete()
