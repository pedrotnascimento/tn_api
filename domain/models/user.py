from werkzeug.security import generate_password_hash, check_password_hash
from infrastructure.db import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    status = db.Column(db.Boolean())

    def __init__(self, username: str, password: str):
        self.username = username
        self.hash_password(password)
        self.status = True

    def __repr__(self):
        return f"<User {self.username}>"

    def hash_password(self, password):
        self.password = generate_password_hash(password) if password is not None else None

    def check_password(self, password):
        return check_password_hash(self.password, password)
