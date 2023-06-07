import unittest
from domain.business_logic.operations.division_operation_action import DivisionOperationAction

class TestDivisionOperation(unittest.TestCase):
    def test_division(self):
        operation_action = DivisionOperationAction()
        result = operation_action.operate(6, 2)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
