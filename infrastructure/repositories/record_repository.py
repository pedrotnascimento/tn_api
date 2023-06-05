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


    def get_pagination(self, user_id: int, page: int, per_page: int, order_by: str):
        select_stmt = db.select(Record).where(Record.user_id == user_id)
        if order_by == "desc":
            select_stmt = select_stmt.order_by(Record.date.desc())
        else:
            select_stmt = select_stmt.order_by(Record.date)
        paginated_items = db.paginate(
            select=select_stmt, page=page, per_page=per_page, count=True
        )
        return paginated_items