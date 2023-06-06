import unittest
from domain.business_logic.operations.square_root_operation_action import SquareRootOperationAction


class TestSquareRootOperation(unittest.TestCase):
    def test_square_root(self):
        operation_action = SquareRootOperationAction()
        result = operation_action.operate(64)
        self.assertEqual(result, 8)


if __name__ == "__main__":
    unittest.main()
