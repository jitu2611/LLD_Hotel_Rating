"""
This Class will keep track of User Class
"""
import uuid
from dataclasses import dataclass, field
from uuid import UUID


@dataclass()
class User:
    id: str = field(init=False, repr=True)
    name: str

    def __post_init__(self):
        self.id = str(uuid.uuid4())

    def get_id(self):
        return self.id



