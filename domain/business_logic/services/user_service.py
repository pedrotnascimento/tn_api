from injector import inject
from domain.business_logic.constants import  CONST_USER_BALANCE_FOR_NEW_USERS
from domain.business_logic.services.record_service import RecordService
from domain.models.user import User
from infrastructure.repositories.user_repository import UserRepository
import logging

logger = logging.getLogger("infoLogger")


class UserService:
    @inject
    def __init__(self, 
                 user_repository: UserRepository,
                 record_service: RecordService):
        self.user_repository = user_repository
        self.record_service = record_service

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
    
    def last_record_from_user(self, user_id):
        record = self.record_service.last_record_from_user(user_id)
        if record is not None and record.user_balance is not None:
            return record.user_balance
        
        return CONST_USER_BALANCE_FOR_NEW_USERS

