from flask import jsonify, request
from app import app, injector
from domain.business_logic.services.record_service import RecordService
from domain.models.user import User
import infrastructure.auth as auth


@app.route("/v1/records", methods=["GET"])
@auth.token_required
def get_records(**kwargs):
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))
    order_by = str(request.args.get("order_by", "asc"))

    record_service = injector.get(RecordService)
    user: User = kwargs["user_session"]
    user_id = user.id
    response = record_service.get_pagination(user_id, page, per_page, order_by)
    response_data = []
    for obj in response["data"]:
        response_data.append(
            {
                "user_id": obj.user_id,
                "operation_id": obj.operation_id,
                "id": obj.id,
                "operation_response": obj.operation_response,
                "user_balance": obj.user_balance,
            }
        )
    response["data"] = response_data
    return jsonify(response)
