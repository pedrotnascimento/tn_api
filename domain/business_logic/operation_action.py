from abc import ABC, abstractmethod

from domain.models.operation import Operation


class OperationAction(ABC):
    def __init__(self, operation: Operation):
        self.operation = operation

    @abstractmethod
    def operate(self, *args) -> object:
        pass
