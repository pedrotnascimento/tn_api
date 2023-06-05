from injector import inject
from domain.business_logic.calculator import CalculatorStrategy
from domain.business_logic.operation_factory import OperationFactory
from domain.models.operation import Operation
from domain.models.record import Record
from infrastructure.repositories.operation_repository import OperationRepository
from infrastructure.repositories.record_repository import RecordRepository
from infrastructure.repositories.user_repository import UserRepository


class OperationManager:
    NEW_USER_BALANCE = 10
    @inject
    def __init__(
        self,
        user_repository: UserRepository,
        operation_repository: OperationRepository,
        record_repository: RecordRepository,
        operation_factory: OperationFactory,
    ):
        self.user_repository = user_repository
        self.operation_repository = operation_repository
        self.record_repository = record_repository
        self.operation_factory = operation_factory

    def get_result(self, user_id, operation_id, *arguments):
        operation_instance: Operation = self.operation_repository.get(operation_id)
        operation_action = self.operation_factory.get_operation(operation_instance.type)
        
        result = self.calculate_result(operation_action, *arguments)
        new_balance = self.calculate_new_user_balance(user_id, operation_instance)
        record = Record(
            user_id,
            operation_instance.id,
            operation_instance.cost,
            new_balance,
            result,
        )

        self.record_repository.insert(record)
        return result


    def calculate_result(self, operation_action, *arguments):
        calculator = CalculatorStrategy()
        result = calculator.calculate(operation_action, *arguments)
        return result

    def calculate_new_user_balance(self, user_id, operation_instance):
        last_record: Record = self.record_repository.last_record_from_user(user_id)
        if last_record is not None:
            amount_updated = last_record.user_balance - operation_instance.cost
        else:
            amount_updated = self.NEW_USER_BALANCE - operation_instance.cost
        return amount_updated
