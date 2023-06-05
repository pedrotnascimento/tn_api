from flask import abort
from injector import inject
from domain.models.user import User
from infrastructure.repositories.user_repository import UserRepository


class UserService:
    @inject
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user_by_id(self, id: int):
        user = self.user_repository.get(id)
        return user

    def create_user(self, user: User):
        if user.username is None or user.password is None:
            return None
        
        has_user = self.user_repository.get(user.id)
        if has_user is not None:
            return None
        new_user = self.user_repository.insert(user)
        return new_user
        