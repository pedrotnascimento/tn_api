from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .base import Base

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(128))
    password: Mapped[str] = mapped_column(String())
    status: Mapped[bool] = mapped_column(Boolean())

    def __init__(self, username: str, password: str):
        self.username = username
        self.hash_password(password)
        self.status = True

    def __repr__(self):
        return f"<User {self.username}>"

    def hash_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
