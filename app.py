import logging
from os import environ
from flask import Flask
from flask_migrate import Migrate
from domain.business_logic.services.record_service import RecordService
from domain.business_logic.operations.division_operation_action import (
    DivisionOperationAction,
)
from domain.business_logic.operations.multiplication_operation_action import (
    MultiplicationOperationAction,
)
from domain.business_logic.operations.random_string_operation_action import (
    RandomStringGenerationOperationAction,
)
from domain.business_logic.operations.square_root_operation_action import (
    SquareRootOperationAction,
)
from domain.business_logic.operations.subtraction_operation_action import (
    SubtractionOperationAction,
)
from infrastructure.repositories.operation_repository import OperationRepository
from infrastructure.repositories.record_repository import RecordRepository
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

from infrastructure.db import db

env = environ.get("ENVIRONMENT")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("infoLogger")
logger.setLevel(logging.INFO)

if env == "production":
    logger.info("Production environment settings")
    app.config.from_object("config.ProdConfig")
elif env== "container":
    logger.info("Container environment settings")
    app.config.from_object("config.ContainerConfig")
else:
    logger.info("Development environment settings")
    app.config.from_object("config.DevConfig")

db.init_app(app)
migrate = Migrate(app, db)

from domain.models.user import *
from domain.models.record import *
from domain.models.operation import *
from infrastructure.repositories.user_repository import UserRepository
from domain.business_logic.operation_factory import OperationFactory
from domain.business_logic.operations.addition_operation_action import (
    AdditionOperationAction,
)

from injector import Injector, Module


class AppModule(Module):
    def configure(self, binder):
        operations_used = [
            AdditionOperationAction(),
            SubtractionOperationAction(),
            MultiplicationOperationAction(),
            DivisionOperationAction(),
            RandomStringGenerationOperationAction(),
            SquareRootOperationAction(),
        ]
        op = OperationFactory(operations_used)
        binder.bind(OperationFactory, to=op)
        binder.bind(UserRepository)
        binder.bind(OperationRepository)
        binder.bind(RecordRepository)
        binder.bind(RecordService)


injector = Injector(AppModule())


@app.route("/")
def test_connection():
    return "<p>It's UP</p>"


from routes.users_routes import *
from routes.operations_routes import *
from routes.records_routes import *
from routes.authentication_routes import *

if __name__ == "__main__":
    app.run(debug=True)
