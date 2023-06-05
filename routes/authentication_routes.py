from flask import jsonify
from app import app
import infrastructure.auth as auth


@app.route("/v1/authenticate", methods=["POST"])
def authenticate():
    result = auth.authenticate()
    if result is None:
        return (
            jsonify(
                {
                    "message": "could not verify",
                }
            ),
            401,
        )

    return jsonify(
        {
            "message": "Validated successfully",
            "token": result,
        }
    )
