import unittest
from unittest.mock import MagicMock
from domain.business_logic.operation_manager import OperationManager
from domain.business_logic.operation_factory import OperationFactory
from domain.business_logic.operations.addition_operation_action import (
    AdditionOperationAction,
)
from domain.business_logic.test_utils.repositories_mocked import (
    OperationMockRepository,
    RecordMockRepository,
    UserMockRepository,
)
from domain.models.operation import Operation
from domain.models.record import Record
from domain.models.user import User


class TestManageOperation(unittest.TestCase):
    def setUp(self):
        operator = Operation("addition", 2)
        operator.id = 1
        self.operators = [operator]

        operators_actions = [AdditionOperationAction()]
        self.operation_factory = OperationFactory(operators_actions)
        self.operators_actions = operators_actions

        user1 = User("user1", "pass")
        user1.id = 1
        self.user1 = user1
        user2 = User("user2", "pass")
        user2.id = 2
        self.users = [user1, user2]

    def test_should_operate_an_addition_with_user_without_any_records(self):
        record_repository = RecordMockRepository([])
        insert_spy = MagicMock(wraps=record_repository.insert)
        record_repository.insert = insert_spy

        manager = OperationManager(
            user_repository=UserMockRepository(self.users),
            operation_repository=OperationMockRepository(self.operators),
            record_repository=record_repository,
            operation_factory=self.operation_factory,
        )

        result = manager.get_result(self.user1.id, self.operators[0].type, 1, 2)

        self.assertEqual(result, 3)
        record = record_repository.last_record_from_user(self.user1.id)
        insert_spy.assert_called_once()
        self.assertEqual(record.amount, self.operators[0].cost)
        self.assertEqual(record.user_balance, 8)
        self.assertEqual(record.user_id, self.user1.id)
        self.assertEqual(record.operation_id, self.operators[0].id)

    def test_should_operate_an_addition_with_user_with_one_record(self):
        user_existing_record = Record(1, 1, 3, 8, "3")
        user_existing_record.id = 1
        record_repository = RecordMockRepository([user_existing_record])
        insert_spy = MagicMock(wraps=record_repository.insert)
        record_repository.insert = insert_spy

        manager = OperationManager(
            user_repository=UserMockRepository(self.users),
            operation_repository=OperationMockRepository(self.operators),
            record_repository=record_repository,
            operation_factory=self.operation_factory,
        )

        result = manager.get_result(self.user1.id, self.operators[0].type, 1, 2)

        self.assertEqual(result, 3)
        record = record_repository.last_record_from_user(self.user1.id)
        insert_spy.assert_called_once()
        self.assertEqual(record.amount, self.operators[0].cost)
        self.assertEqual(record.user_balance, 6)
        self.assertEqual(record.user_id, self.user1.id)
        self.assertEqual(record.operation_id, self.operators[0].id)

    def test_should_fail_on_operate_when_user_has_no_credits(self):
        user_existing_record = Record(1, 1, 3, 0, "3")
        user_existing_record.id = 1
        record_repository = RecordMockRepository([user_existing_record])
        insert_spy = MagicMock(wraps=record_repository.insert)
        record_repository.insert = insert_spy

        manager = OperationManager(
            user_repository=UserMockRepository(self.users),
            operation_repository=OperationMockRepository(self.operators),
            record_repository=record_repository,
            operation_factory=self.operation_factory,
        )

        result = manager.get_result(self.user1.id, self.operators[0].type, 1, 2)

        self.assertEqual(result, None)
        insert_spy.assert_not_called()


if __name__ == "__main__":
    unittest.main()
