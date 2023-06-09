from injector import inject
from domain.models.record import Record
import logging
from infrastructure.db import db
from infrastructure.repositories.record_repository import RecordRepository


logger = logging.getLogger("infoLogger")


class RecordService:
    @inject
    def __init__(self, record_repository: RecordRepository):
        self.record_repository = record_repository

    def get_pagination(
        self,
        user_id: int,
        page: int,
        per_page: int,
        order_field: str,
        order_direction: str,
        filter_field: str,
        filter_value: str,
    ):
        paginated_items = self.record_repository.get_pagination(
            user_id,
            page,
            per_page,
            order_field,
            order_direction,
            filter_field,
            filter_value,
        )

        response = {
            "page": paginated_items.page,
            "perPage": paginated_items.per_page,
            "totaltems": paginated_items.total,
            "data": paginated_items.items,
            "pages": paginated_items.pages,
        }
        return response

    def last_record_from_user(self, user_id):
        user = self.record_repository.last_record_from_user(user_id)
        return user

    def soft_delete(self, record_id):
        self.record_repository.soft_delete(record_id)
