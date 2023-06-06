import unittest
from domain.business_logic.operations.multiplication_operation_action import MultiplicationOperationAction


class TestmultiplicationOperation(unittest.TestCase):
    def test_multiplication(self):
        operation_action = MultiplicationOperationAction()
        result = operation_action.operate(3, 2)
        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()
