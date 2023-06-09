from app import app, injector
from flask import abort, request
from flask import jsonify
import infrastructure.auth as auth
from domain.models.user import User
from domain.business_logic.operation_manager import OperationManager


@app.route("/v1/operations", methods=["POST"])
@auth.token_required
def make_operation(**kwargs):
    if request.is_json:
        data = request.get_json()
        operation_manager: OperationManager = injector.get(OperationManager)
        user: User = kwargs["user_session"]
        user_id = user.id
        operation_type = data["operationType"]
        arguments = tuple(data["arguments"])
        if user_id is None:
            abort(400)
        if operation_type is None:
            abort(400)

        response = operation_manager.get_result(user_id, operation_type, *arguments)
        if response == OperationManager.CODE_NO_BALANCE:
            return jsonify({"error": response}), 400
        if response is None:
            abort(400)
        return jsonify({"result": response}), 201
    else:
        return {"error": "The request payload is not in JSON format"}
