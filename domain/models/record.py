from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from domain.models.user import User

class Record(Base):
    __tablename__ = "record"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    operation_id: Mapped[int]  = mapped_column(ForeignKey("operation.id"))

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    amount: Mapped[int]
    user_balance: Mapped[int]
    operation_response: Mapped[str]
    status: Mapped[bool]

    def __init__(self,user_id: int,  
                 operation_id: int, 
                 amount: int, 
                 user_balance: int, 
                 operation_response: str):
        self.operation_id = operation_id
        self.user_id = user_id
        self.amount = amount
        self.user_balance = user_balance
        self.operation_response = operation_response
        self.status = True

    def __repr__(self):
        return f"""<record 
      {self.id}, {self.operation_id}, {self.user_id}, 
      {self.amount}, {self.user_balance}, {self.operation_response}, 
      {self.status}>"""
