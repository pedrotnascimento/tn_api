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

    def get_pagination(
        self,
        user_id: int,
        page: int,
        per_page: int,
        order_field: str,
        order_direction: str,
    ):
        dict_field ={
            "id": Record.id,
            "operationType": Operation.type,
            "operationResponse": Record.operation_response,
            "userBalance": Record.user_balance,
            "date": Record.date,
        }
        
        select_stmt = (
            db.session.query(Record, Operation, User)
            .where(Record.user_id == user_id, Record.status==True)
            .join(Operation)
            .join(User)
            .add_columns(Operation.type, Operation.id, User.username, Operation.id)
        )

        if order_field!= "":
            
            if  order_direction == "desc":
                select_stmt = select_stmt.order_by(dict_field[order_field].desc())
            else:
                select_stmt = select_stmt.order_by(dict_field[order_field])
        else:
             select_stmt.order_by(Record.id)
        
        paginated_items = select_stmt.paginate(page=page, per_page=per_page, count=True)
        
        return paginated_items

    def soft_delete(self, record_id):
        item:Record = Record.query.where(record_id==Record.id).first()
        if not item:
            return 
        item.status = False
        db.session.commit()
            