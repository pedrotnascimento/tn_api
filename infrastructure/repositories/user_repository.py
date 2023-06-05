
from domain.models.user import User
from infrastructure.repositories.base_repository import BaseRepository
from infrastructure.db import db
class UserRepository(BaseRepository):
    def get(self, id: int):
        user = User.query.get(id)

        if user:
            response = {
                "id": user.id,
                "username": user.username,
                "status": user.status,
            }
            return {"message": "success", "user": response}

    def get_by_name(self, username: str):
        user = User.query.filter_by(username=username).first()
        return user

    def insert(self, user: User):
        db.session.add(user)
        db.session.commit()

    def update(self, id: int):
        pass

    def delete(self, id: int):
        pass
