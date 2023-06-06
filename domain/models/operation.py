from infrastructure.db import db

class Operation(db.Model):
    __tablename__ = "operation"

    id=db.Column(db.Integer(), primary_key=True)
    type = db.Column(db.String())
    cost = db.Column(db.Integer())
    status = db.Column(db.Boolean())
    records = db.relationship('Record', backref='operation')

    def __init__(self, type: str, cost: int):
        self.type = type
        self.cost = cost
        self.status = True

    def __repr__(self):
        return f"<Operation {self.id}, {self.type}, {self.cost}>"
