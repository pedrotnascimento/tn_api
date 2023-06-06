from domain.business_logic.operation_action_abstract import OperationActionAbstract


class DivisionOperationAction(OperationActionAbstract):
    def __init__(self):
        self.type = "division"

    def operate(self, a: float, b: float) -> float:
        return float(a) / float(b)
