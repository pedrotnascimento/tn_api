from domain.models.record import Record
from infrastructure.repositories.base_repository import BaseRepository


class RecordRepository(BaseRepository):
    def get()-> Record:
        pass

    def last_record_from_user(self,user_id)-> Record:
        pass

    def insert(record: Record):
        pass