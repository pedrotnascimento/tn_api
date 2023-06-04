from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .base import Base
from abc import ABC, abstractmethod

class Operation(Base):
    __tablename__ = "operation"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str]
    cost: Mapped[int]
    status: Mapped[bool]

    def __init__(self, type: str, cost: int):
        self.type = type
        self.cost = cost
        self.status = True

    def __repr__(self):
        return f"<Operation {self.type}, {self.cost}>"
