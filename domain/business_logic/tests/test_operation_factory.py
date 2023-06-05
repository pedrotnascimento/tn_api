import unittest
from domain.business_logic.operation_factory import OperationFactory
from domain.business_logic.operations.addition_operation_action import AdditionOperationAction
from domain.models.operation import Operation


class TestOperationFactory(unittest.TestCase):
    def test_should_get_a_operation(self):

        operation_action = AdditionOperationAction()
        operation_factory = OperationFactory([operation_action])
        result = operation_factory.get_operation("addition")

        self.assertEqual(result.type, "addition")
        self.assertTrue(result is operation_action)


if __name__ == "__main__":
    unittest.main()
