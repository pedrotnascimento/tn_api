from domain.business_logic.operation_action import OperationAction


class CalculatorStrategy:
    def calculate(self, operation: OperationAction, *args):        
        return operation.operate(*args)
