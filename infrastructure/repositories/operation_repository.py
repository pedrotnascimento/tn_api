from domain.models.operation import Operation
from infrastructure.repositories.base_repository import BaseRepository


class OperationRepository(BaseRepository):
    def get(self, id: int):
        operation = Operation.query.get(id)
        return operation

    def get_by_type(self, type: str):
        operation = Operation.query.filter_by(type=type).first()
        if operation:
            return operation

