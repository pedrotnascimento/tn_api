import unittest
from unittest.mock import MagicMock
from domain.business_logic.services.user_service import UserService
from domain.business_logic.test_utils.repositories_mocked import (
    UserMockRepository,
)
from domain.models.user import User


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
        user_service = UserService(user_repo)
        user = User("test", "123")

        user_service.create_user(user)

        insert_spy.assert_called_once_with(user)

    def test_should_return_none_if_username_empty(self):
        user_repo = UserMockRepository(self.users)
        insert_spy = MagicMock(wraps=user_repo.insert)
        user_repo.insert = insert_spy
        user_service = UserService(user_repo)
        user = User(None, "123")

        response = user_service.create_user(user)
        self.assertIsNone(response)
        insert_spy.assert_not_called()

    def test_should_return_none_if_password_empty(self):
        user_repo = UserMockRepository(self.users)
        insert_spy = MagicMock(wraps=user_repo.insert)
        user_repo.insert = insert_spy
        user_service = UserService(user_repo)
        user = User("teste", None)

        response = user_service.create_user(user)
        self.assertIsNone(response)
        insert_spy.assert_not_called()


if __name__ == "__main__":
    unittest.main()
