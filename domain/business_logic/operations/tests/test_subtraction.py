import unittest
from domain.business_logic.operations.subtraction_operation_action import (
    SubtractionOperationAction,
)

class TestSubtractionOperation(unittest.TestCase):
    def test_subtraction(self):
        operation_action = SubtractionOperationAction()
        result = operation_action.operate(5, 1)
        self.assertEqual(result, 4)


if __name__ == "__main__":
    unittest.main()
