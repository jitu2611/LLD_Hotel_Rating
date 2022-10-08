"""
This will manage the database for our project
In-memory Database we will use
"""
from dataclasses import dataclass,field
from typing import Dict


@dataclass()
class Database:

    user_id_mapping: Dict = field(init=False, default_factory=dict)
    hotel_id_mapping: Dict = field(init=False, default_factory=dict)
    rating_id_mapping: Dict = field(init=False, default_factory=dict)
    hotel_rating_list: Dict = field(init=False, default_factory=dict)

    def add_user_to_database(self, user1):
        self.user_id_mapping[user1.get_id()] = user1

    def add_hotel_to_database(self, hotel1):
        self.hotel_id_mapping[hotel1.get_id()] = hotel1
        self.hotel_rating_list[hotel1.get_id()] = dict()

    def get_hotel_obj(self, hotel_id):
        return self.hotel_id_mapping[hotel_id]

    def get_rating_obj(self, rating_id):
        return self.rating_id_mapping[rating_id]

    def get_all_hotels_list(self):
        return self.hotel_rating_list

    def add_rating_to_database(self, rating):
        hotel_id = rating.get_hotel_id()
        user_id = rating.get_user_id()
        hotel_obj = self.hotel_id_mapping[hotel_id]

        curr_rating = hotel_obj.get_rating()

        self.rating_id_mapping[rating.get_id()] = rating

        num = len(self.hotel_rating_list[hotel_id])
        if user_id not in self.hotel_rating_list[hotel_id]:
            new_rating = ((curr_rating * num) + rating.get_rating()) / (num + 1)
        else:
            get_prev_rating_user = self.rating_id_mapping[self.hotel_rating_list[hotel_id][user_id]].get_rating()
            new_rating = ((curr_rating * num) - get_prev_rating_user + rating.get_rating()) / num

        self.hotel_rating_list[hotel_id][user_id] = rating.get_id()

        hotel_obj.set_rating(new_rating)




