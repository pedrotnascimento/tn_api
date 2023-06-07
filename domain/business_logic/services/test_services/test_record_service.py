import unittest
from unittest.mock import MagicMock
from domain.business_logic.services.user_service import UserService
from domain.business_logic.test_utils.repositories_mocked import (
    RecordMockRepository,
    UserMockRepository,
)
from domain.models.record import Record
from domain.models.user import User


class TestRecordService(unittest.TestCase):
    def test_should_return_last_record_given_user_id_when_user_has_records(self):
        user_balance = 4
        records = [Record(1, 1, 3, user_balance=user_balance, operation_response="any")]
        record_repo = RecordMockRepository(records)

        last_record = record_repo.last_record_from_user(1)
        self.assertEqual(last_record.user_balance, user_balance)

    def test_should_return_none_if_there_is_no_last_record(self):
        user_balance = 4
        record_repo = RecordMockRepository([])

        last_record = record_repo.last_record_from_user(1)
        self.assertIsNone(last_record)



if __name__ == "__main__":
    unittest.main()
