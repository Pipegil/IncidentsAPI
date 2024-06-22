from typing import List
from uuid import UUID

from google.cloud.firestore_v1 import FieldFilter

from firestorefastapi.database import db
from firestorefastapi.schemas.user import User, UserCreate, UserUpdate


class UserDAO:
    collection_name = "users"

    def create(self, user_create: UserCreate) -> User:
        data = user_create.dict()
        data["id"] = str(data["id"])
        doc_ref = db.collection(self.collection_name).document(str(user_create.id))
        doc_ref.set(data)
        return self.get(user_create.id)

    def get(self, id: UUID) -> User:
        doc_ref = db.collection(self.collection_name).document(str(id))
        doc = doc_ref.get()
        if doc.exists:
            return User(**doc.to_dict())
        return

    def get_by_email(self, email: str):
        users_ref = db.collection(self.collection_name)
        docs = users_ref.where(filter=FieldFilter('email', '==', email)).stream()
        for doc in docs:
            return User(**doc.to_dict())
        return None

    def list(self) -> List[User]:
        users_ref = db.collection(self.collection_name)
        return [
            User(**doc.get().to_dict())
            for doc in users_ref.list_documents()
            if doc.get().to_dict()
        ]

    def update(self, id: UUID, user_update: UserUpdate) -> User:
        data = user_update.dict()
        doc_ref = db.collection(self.collection_name).document(str(id))
        doc_ref.update(data)
        return self.get(id)

    def delete(self, id: UUID) -> None:
        db.collection(self.collection_name).document(str(id)).delete()
