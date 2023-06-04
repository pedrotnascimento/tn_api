import unittest
from domain.business_logic.operators.addition_operator import AdditionOperator
from domain.models.operation import Operation


class TestAdditionOperator(unittest.TestCase):
    def test_addition(self):
        operator_data = Operation("addition", 2)
        operator_action = AdditionOperator(operator_data)
        result = operator_action.operate(1, 2)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
