from typing import List
from uuid import UUID

from fastapi import HTTPException

from firestorefastapi.dao.user import UserDAO
from firestorefastapi.schemas.user import User, UserCreate, UserUpdate, UserLogin

user_dao = UserDAO()


class UserService:
    def create_user(self, user_create: UserCreate) -> User:
        return user_dao.create(user_create)

    def get_user(self, id: UUID) -> User:
        return user_dao.get(id)

    def list_users(self) -> List[User]:
        return user_dao.list()

    def update_user(self, id: UUID, user_update: UserUpdate) -> User:
        return user_dao.update(id, user_update)

    def delete_user(self, id: UUID) -> None:
        return user_dao.delete(id)

    def login(self, user_login: UserLogin) -> User:
        user = user_dao.get_by_email(user_login.email)
        if not user or user.password != user_login.password:
            raise HTTPException(status_code=400, detail="Invalid login credentials")
        return user
