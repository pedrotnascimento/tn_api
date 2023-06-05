from domain.business_logic.operation_action_abstract import OperationActionAbstract


class AdditionOperationAction(OperationActionAbstract):
    def __init__(self):
        self.type = "addition"

    def operate(self, a: float, b: float) -> float:
        return a + b
