from domain.business_logic.operation_action_abstract import OperationActionAbstract


class CalculatorStrategy:
    def calculate(self, operation: OperationActionAbstract, *args):        
        return operation.operate(*args)
