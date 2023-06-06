from injector import inject
from domain.models.operation import Operation
from domain.models.record import Record
from domain.models.user import User
from infrastructure.db import db
from infrastructure.repositories.operation_repository import OperationRepository
from infrastructure.repositories.user_repository import UserRepository


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
        select_stmt = (
            db.session.query(Record, Operation, User)
            .where(Record.user_id == user_id)
            .join(Operation)
            .join(User)
            .add_columns(Operation.type, Operation.id, User.username, Operation.id)
        )

        if order_by == "desc":
            select_stmt = select_stmt.order_by(Record.date.desc())
        else:
            select_stmt = select_stmt.order_by(Record.date)
        paginated_items = select_stmt.paginate(page=page, per_page=per_page, count=True)

        return paginated_items
