from injector import inject
from domain.models.user import User
from infrastructure.repositories.user_repository import UserRepository
import logging
logger = logging.getLogger("infoLogger")
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
        logger.info("RECEIVING USER")
        has_user = self.user_repository.get_by_name(user.username)
        logger.info("CHECKING USER")
        if has_user is not None:
            return None
        logger.info("CREATING USER")
        new_user = self.user_repository.insert(user)
        logger.info("USER CREATED")
        return new_user
        