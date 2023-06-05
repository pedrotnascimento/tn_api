from domain.models.record import Record
from infrastructure.db import db


class RecordRepository:
    def get() -> list[Record]:
        return Record.query.all()

    def last_record_from_user(self, user_id) -> Record:
        record = (
            Record.query.filter_by(user_id=user_id).order_by(Record.date.desc()).first()
        )
        if record:
            return record

    def insert(self, record: Record):
        db.session.add(record)
        db.session.commit()
