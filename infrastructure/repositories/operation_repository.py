from domain.models.operation import Operation
from infrastructure.repositories.base_repository import BaseRepository


class OperationRepository(BaseRepository):
    def get(id: int) -> Operation:
        pass