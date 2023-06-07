import unittest
from unittest.mock import MagicMock
from app import CONST_USER_BALANCE_FOR_NEW_USERS
from domain.business_logic.services.record_service import RecordService
from domain.business_logic.services.user_service import UserService
from domain.business_logic.test_utils.repositories_mocked import (
    RecordMockRepository,
    UserMockRepository,
)
from domain.models.record import Record
from domain.models.user import User
from infrastructure.repositories.record_repository import RecordRepository


class TestUserService(unittest.TestCase):
    def setUp(self):
        user1 = User("user1", "pass")
        user1.id = 1
        self.user1 = user1
        user2 = User("user2", "pass")
        user2.id = 2
        self.users = [user1, user2]

    def test_should_create_user(self):
        user_repo = UserMockRepository(self.users)
        insert_spy = MagicMock(wraps=user_repo.insert)
        user_repo.insert = insert_spy
        user_service = UserService(user_repo,None)
        user = User("test", "123")

        user_service.create_user(user)

        insert_spy.assert_called_once_with(user)

    def test_should_return_none_if_username_empty(self):
        user_repo = UserMockRepository(self.users)
        insert_spy = MagicMock(wraps=user_repo.insert)
        user_repo.insert = insert_spy
        user_service = UserService(user_repo,None)
        user = User(None, "123")

        response = user_service.create_user(user)
        self.assertIsNone(response)
        insert_spy.assert_not_called()

    def test_should_return_none_if_password_empty(self):
        user_repo = UserMockRepository(self.users)
        insert_spy = MagicMock(wraps=user_repo.insert)
        user_repo.insert = insert_spy
        user_service = UserService(user_repo,None)
        user = User("teste", None)

        response = user_service.create_user(user)
        self.assertIsNone(response)
        insert_spy.assert_not_called()

    def test_should_return_user_balance_if_there_is_record(self):
        user_balance = 4
        record_repository = RecordMockRepository([Record(1,1,1,user_balance=user_balance,operation_response="")])
        record_service = RecordService(record_repository)
        user_repo = UserMockRepository(self.users)
        user_service = UserService(user_repo, record_service)
        
        user_balance_result  = user_service.last_record_from_user(1)
        self.assertEqual(user_balance_result, user_balance)
   
    def test_should_return_default_user_balance_if_there_is_no_record(self):
        record_repository = RecordMockRepository([])
        record_service = RecordService(record_repository)
        user_repo = UserMockRepository(self.users)
        user_service = UserService(user_repo, record_service)
        
        user_balance_result  = user_service.last_record_from_user(1)
        self.assertEqual(user_balance_result, CONST_USER_BALANCE_FOR_NEW_USERS)

if __name__ == "__main__":
    unittest.main()
