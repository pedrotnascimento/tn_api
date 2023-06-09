from domain.models.user import User
from infrastructure.db import db


class UserRepository:
    def get(self, id: int):
        user = User.query.get(id)
        if user:
            return user

    def get_by_name(self, username: str):
        user = User.query.filter_by(username=username).first()
        if user:
            return user

    def insert(self, user: User):
        db.session.add(user)
        res = db.session.commit()
        return user
        
