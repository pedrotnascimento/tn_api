from flask import jsonify, request
from app import app, injector
from domain.business_logic.services.record_service import RecordService
from domain.models.user import User
import infrastructure.auth as auth


@app.route("/v1/records", methods=["GET"])
@auth.token_required
def get_records(**kwargs):
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("perPage", 10))
    order_by_field = str(request.args.get("sortField", ""))
    order_by_direction = str(request.args.get("sortDirection", "asc"))
    filter_field = str(request.args.get("filterField", ""))
    filter_value = str(request.args.get("filterValue", ""))

    record_service = injector.get(RecordService)
    user: User = kwargs["user_session"]
    user_id = user.id

    response = record_service.get_pagination(
        user_id,
        page,
        per_page,
        order_by_field,
        order_by_direction,
        filter_field,
        filter_value,
    )
    response_data = []
    for obj in response["data"]:
        response_data.append(
            {
                "userId": obj[0].user_id,
                "operationId": obj[0].operation_id,
                "operationType": obj[1].type,
                "userName": obj[2].username,
                "id": obj[0].id,
                "operationResponse": obj[0].operation_response,
                "userBalance": obj[0].user_balance,
            }
        )
    response["data"] = response_data
    return jsonify(response)


@app.route("/v1/records/<record_id>", methods=["DELETE"])
@auth.token_required
def delete_records(record_id, **kwargs):
    record_service: RecordService = injector.get(RecordService)
    record_service.soft_delete(record_id)
    return jsonify({}), 200
