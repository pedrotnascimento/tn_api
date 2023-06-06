import unittest
from domain.business_logic.operations.addition_operation_action import AdditionOperationAction


class TestAdditionOperation(unittest.TestCase):
    def test_addition(self):
        operation_action = AdditionOperationAction()
        result = operation_action.operate(1, 2)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
