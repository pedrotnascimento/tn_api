import math
from domain.business_logic.operation_action_abstract import OperationActionAbstract


class SquareRootOperationAction(OperationActionAbstract):
    def __init__(self):
        self.type = "square_root"

    def operate(self, a: float) -> float:
        return math.sqrt(float(a))
