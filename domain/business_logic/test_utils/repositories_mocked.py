from domain.models.operation import Operation
from domain.models.record import Record
from domain.models.user import User


class RecordMockRepository:
    def __init__(self, instances):
        self.instances: list[object] = instances

    def get() -> Record:
        pass

    def last_record_from_user(self, user_id) -> Record:
        instances = list(filter(lambda x: x.user_id == user_id, self.instances))
        instances_sorted = sorted(instances, key=lambda x: x.id, reverse=True)
        
        return instances_sorted[0] if len(instances_sorted) else None

    def insert(self, instance: Record):
        instance.id = len(self.instances) + 1
        self.instances.append(instance)

    def delete(self, id):
        self.instances = filter(lambda x: x.id != id, self.instances)

    def update(self, instance: Record):
        instances_temp = filter(lambda x: x.id != instance.id, self.instances)
        instances_temp.append(instance)
        self.instances = instances_temp


class UserMockRepository:
    def __init__(self, instances):
        self.instances: list[object] = instances

    def get(self, id: int) -> User:
        instances = list(filter(lambda x: x.id == id, self.instances))
        return instances[0] if len(instances) else None

    def insert(self, instance: User):
        instance.id = len(self.instances) + 1
        self.instances.append(instance)

    def delete(self, id):
        self.instances = filter(
            lambda x: x.id != id,
            self.instances,
        )

    def update(self, instance: User):
        instances_temp = filter(lambda x: x.id != instance.id, self.instances)
        instances_temp.append(instance)
        self.instances = instances_temp

    def get_by_name(self, username: str):
        instances = list(
            filter(
                lambda x: x.username == username,
                self.instances,
            )
        )
        return instances[0] if len(instances) else None


class OperationMockRepository:
    def __init__(self, instances):
        self.instances: list[object] = instances

    def get(self, id: int) -> Operation:
        instances = list(filter(lambda x: x.id == id, self.instances))
        return instances[0] if len(instances) else None

    def insert(self, instance: Operation):
        instance.id = len(self.instances) + 1
        self.instances.append(instance)

    def delete(self, id):
        self.instances = filter(
            lambda x: x.id != id,
            self.instances,
        )

    def update(self, instance: Operation):
        instances_temp = filter(
            lambda x: x.id != instance.id,
            self.instances,
        )
        instances_temp.append(instance)
        self.instances = instances_temp

    def get_by_type(self, type):
        instances = list(filter(lambda x: x.type == type, self.instances))
        return instances[0] if len(instances) else None        
