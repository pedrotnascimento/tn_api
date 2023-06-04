import unittest
from domain.business_logic.operations.addition_operation import AdditionOperation
from domain.models.operation import Operation


class TestAdditionOperation(unittest.TestCase):
    def test_addition(self):
        operation_data = Operation("addition", 2)
        operation_action = AdditionOperation(operation_data)
        result = operation_action.operate(1, 2)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
