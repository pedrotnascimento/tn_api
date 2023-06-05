import datetime
from functools import wraps
from app import app
from flask import request, jsonify
import jwt
from werkzeug.security import check_password_hash

from .repositories.user_repository import UserRepository


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "Authorization" not in request.headers:
            return jsonify({"message": "token is missing", "data": []}), 401
        token = request.headers["Authorization"]

        if not token:
            return jsonify({"message": "token is missing", "data": []}), 401
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"])
            username = data["username"]
            user_repository = UserRepository()
            current_user = user_repository.get_by_name(username)
        except:
            return jsonify({"message": "token is invalid or expired", "data": []}), 401
        return f(current_user, *args, **kwargs)

    return decorated


# Gerando token com base na Secret key do app e definindo expiração com 'exp'
def authenticate():
    if not request.is_json:
        return jsonify({"message": "Wrong data format type"}), 401

    auth = request.get_json()
    username = auth["username"]
    password = auth["password"]
    if not auth or not username or not password:
        return None
    user_repository = UserRepository()
    current_user = user_repository.get_by_name(username)
    if not current_user:
        return None

    if current_user and check_password_hash(current_user.password, password):
        token = jwt.encode(
            {
                "username": current_user.username,
                "exp": datetime.datetime.now() + datetime.timedelta(hours=12),
            },
            app.config["SECRET_KEY"],
        )
        return token

    return (
        jsonify(
            {
                "message": "could not verify",
                "WWW-Authenticate": 'Basic auth="Login required"',
            }
        ),
        401,
    )
