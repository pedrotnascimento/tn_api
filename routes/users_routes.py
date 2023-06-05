from app import app, injector
from flask import abort, request
from flask import jsonify
from domain.business_logic.services.user_service import UserService

from domain.models.user import User


@app.route("/v1/users", methods=["POST"])
def create_user():
    if request.is_json:
        data = request.get_json()
        user_service: UserService = injector.get(UserService)
        user = User(username=data["username"], password=data["password"])
        response = user_service.create_user(user)
        if response is None:
            abort(400)
        return jsonify({"username": user.username}), 201
    else:
        return {"error": "The request payload is not in JSON format"}
