from domain.business_logic.operation_action import OperationAction
from domain.models.operation import Operation


class OperationFactory:
    def __init__(self, operations: list[OperationAction]):
        self.operations_dict: OperationAction = {}
        for i in operations:
            self.operations_dict[i.operation.type] = i

    def create(self, operation_type: str) -> OperationAction:
        if operation_type in self.operations_dict:
            return self.operations_dict[operation_type]
        return None
