import unittest
from domain.business_logic.operations.random_string_operation_action import RandomStringGenerationOperationAction

class TestRandomStringGenerationOperation(unittest.TestCase):
    def test_random_string_generation(self):
        operation_action = RandomStringGenerationOperationAction()
        result = operation_action.operate()
        self.assertEqual(type(result), str)


if __name__ == "__main__":
    unittest.main()
