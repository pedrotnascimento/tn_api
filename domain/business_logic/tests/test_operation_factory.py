import unittest
from domain.business_logic.operation_factory import OperationFactory
from domain.business_logic.operations.addition_operation import AdditionOperation
from domain.models.operation import Operation


class TestOperationFactory(unittest.TestCase):
    def test_should_get_a_operation(self):
        operation_data = Operation("addition", 2)
        operation_action = AdditionOperation(operation_data)
        operation_factory = OperationFactory([operation_action])
        result = operation_factory.create("addition")

        self.assertEqual(result.operation.type, "addition")
        self.assertEqual(result.operation.cost, 2)
        self.assertTrue(result.operation is operation_data)
        self.assertTrue(result is operation_action)


if __name__ == "__main__":
    unittest.main()
