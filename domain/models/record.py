from infrastructure.db import db
from datetime import datetime as dt

class Record(db.Model):
    __tablename__ = "record"

    id = db.Column(db.Integer(), primary_key=True)
    operation_id = db.Column(db.Integer(), db.ForeignKey('operation.id'))
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    amount = db.Column(db.Integer())
    user_balance = db.Column(db.Integer())
    operation_response = db.Column(db.String())
    status = db.Column(db.Boolean())
    date = db.Column(db.DateTime())

    def __init__(
        self,
        user_id: int,
        operation_id: int,
        amount: int,
        user_balance: int,
        operation_response: str,
    ):
        self.operation_id = operation_id
        self.user_id = user_id
        self.amount = amount
        self.user_balance = user_balance
        self.operation_response = operation_response
        self.status = True
        self.date = dt.now()

    def __repr__(self):
        return f"""<record 
      {self.id}, {self.operation_id}, {self.user_id}, 
      {self.amount}, {self.user_balance}, {self.operation_response}, 
      {self.status}>"""
