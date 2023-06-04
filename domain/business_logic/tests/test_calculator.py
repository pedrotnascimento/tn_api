import unittest
from domain.business_logic.calculator import CalculatorStrategy
from domain.business_logic.operation_factory import OperationFactory
from domain.business_logic.operations.addition_operation import AdditionOperation
from domain.models.operation import Operation


class TestCalculator(unittest.TestCase):
    def test_should_calculate_a_operation(self):
        operation_data = Operation("addition", 2)
        operation_action = AdditionOperation(operation_data)
        calculator = CalculatorStrategy()
        result = calculator.calculate(operation_action, 1, 2)

        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
