from domain.business_logic.operation_action_abstract import OperationActionAbstract


class OperationFactory:
    def __init__(self, operations: list[OperationActionAbstract]):
        self.operations_dict: OperationActionAbstract = {}
        for i in operations:
            self.operations_dict[i.type] = i

    def get_operation(self, operation_type: str) -> OperationActionAbstract:
        if operation_type in self.operations_dict:
            return self.operations_dict[operation_type]
        return None
