from domain.business_logic.operation_action import OperationAction
from domain.models.operation import Operation


class AdditionOperator(OperationAction):
    def __init__(self, operation: Operation):
        super().__init__(operation)

    def operate(self, a: float, b: float)->float:
        return a + b