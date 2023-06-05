from abc import ABC, abstractmethod

from domain.models.operation import Operation


class OperationActionAbstract(ABC):
    @abstractmethod
    def operate(self, *args) -> object:
        pass
