from app import app, injector
from flask import abort, request
from flask import jsonify
from domain.business_logic.services.record_service import RecordService
from domain.business_logic.services.user_service import UserService
import infrastructure.auth as auth
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


@app.route("/v1/users/balance", methods=["GET"])
@auth.token_required
def get_user_balance(**kwargs):
    user = kwargs["user_session"]
    user_id = user.id
    user_service = injector.get(UserService)
    user_balance = user_service.last_record_from_user(user_id)
    
    if user_balance is None:
        abort(400)
    return jsonify({"userBalance": user_balance}), 200
