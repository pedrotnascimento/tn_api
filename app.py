from flask import Flask
from flask_migrate import Migrate


app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:example@localhost:5432/db_local"
from infrastructure.db import db

db.init_app(app)
migrate = Migrate(app, db)

from injector import Injector, Module

from domain.models.user import *
from domain.models.record import *
from domain.models.operation import *
from infrastructure.repositories.user_repository import UserRepository
from domain.business_logic.operation_factory import OperationFactory
from domain.business_logic.operations.addition_operation_action import (
    AdditionOperationAction,
)


class AppModule(Module):
    def configure(self, binder):
        operations_used = [AdditionOperationAction()]
        op = OperationFactory(operations_used)
        binder.bind(UserRepository)
        binder.bind(OperationFactory, to=op)


injector = Injector(AppModule())


@app.route("/")
def test_connection():
    return "<p>It's UP</p>"


from routes.users_routes import *

if __name__ == "__main__":
    app.run(debug=True)
