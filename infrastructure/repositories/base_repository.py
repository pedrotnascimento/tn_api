from abc import ABC, abstractmethod

class BaseRepository(ABC):
    @abstractmethod
    def get(id: int):
        pass
    @abstractmethod
    def insert(id: int):
        pass
    @abstractmethod
    def update(id: int):
        pass
    @abstractmethod
    def delete(id: int):
        pass
