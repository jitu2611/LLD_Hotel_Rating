"""
This class will represent all the Hotels
"""
import uuid
from dataclasses import dataclass, field


@dataclass()
class Hotel:
    id: str = field(init=False, repr=False)
    name: str
    rating: float = field(init=False, repr=True, default=0)
    plus_size: bool = field(default=0)

    def __post_init__(self):
        self.id = str(uuid.uuid4())

    def get_id(self):
        return self.id

    def get_rating(self):
        return self.rating

    def set_rating(self, rating):
        self.rating = rating



