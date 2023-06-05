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

    def get_pagination(self, user_id: int, page: int, per_page: int, order_by: str):
        paginated_items = self.record_repository.get_pagination(
            user_id, page, per_page, order_by
        )

        response = {
            "page": paginated_items.page,
            "per_page": paginated_items.per_page,
            "total_items": paginated_items.total,
            "data": paginated_items.items,
            "pages": paginated_items.pages,
        }
        return response
