"""
This class will manage the Rating ( given by user to particular Hotel )
"""
import uuid
from dataclasses import dataclass, field
from uuid import UUID
from datetime import datetime


@dataclass()
class Rating:
    id: str = field(init=False, repr=True)
    user_id: UUID
    hotel_id: UUID
    rating: float
    review: str
    date: datetime = field(init=False, repr=True)

    def __post_init__(self):
        self.id = str(uuid.uuid4())
        self.date = datetime.now()

    def get_id(self):
        return self.id

    def get_rating(self):
        return self.rating

    def get_review(self):
        return self.review

    def get_date(self):
        return self.date

    def get_hotel_id(self):
        return self.hotel_id

    def get_user_id(self):
        return self.user_id



