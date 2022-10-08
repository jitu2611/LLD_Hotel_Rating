"""
This is Service CLass, which interacts with Database and gets the result for Driver Class
"""
from dataclasses import dataclass
from database import Database


@dataclass()
class Service:
    database: Database

    @staticmethod
    def print_hotels(hotels):
        for hotel in hotels:
            print(hotel)

    @staticmethod
    def print_rating(list_of_rating_obj):
        for rating in list_of_rating_obj:
            print(f'{rating.get_rating()}, {rating.get_review()}, {rating.get_date()}')

    def find_all_hotels(self, _filter=None, _order=None):
        list_of_hotels = self.database.get_all_hotels_list()
        list_of_hotel_obj = list(map(lambda x: self.database.get_hotel_obj(x), list_of_hotels))

        if _filter:
            list_of_hotel_obj = list(filter(lambda x: x.get_rating() > _filter
                                            , list_of_hotel_obj))

        if _order:

            if "ASC" in _order:
                list_of_hotel_obj = sorted(list_of_hotel_obj, key=lambda x: x.rating)
            else:
                list_of_hotel_obj = sorted(list_of_hotel_obj, key=lambda x: x.rating, reverse=True)

        list_of_hotel_obj = sorted(list_of_hotel_obj, key=lambda x: x.plus_size, reverse=True)

        self.print_hotels(list_of_hotel_obj)

    def find_all_ratings(self, hotel_id, _filter=None, _order=None):
        list_of_rating = self.database.get_all_hotels_list()[hotel_id]
        list_of_rating_obj = list(map(lambda x: self.database.get_rating_obj(x), list(list_of_rating.values())))

        if _filter:
            list_of_rating_obj = list(filter(lambda x: x.get_rating() >= _filter
                                             , list_of_rating_obj))

        if _order:
            if "ASC" in _order:
                list_of_rating_obj = sorted(list_of_rating_obj, key=lambda x: x.rating)
            else:
                list_of_rating_obj = sorted(list_of_rating_obj, key=lambda x: x.rating, reverse=True)
        else:
            list_of_rating_obj = sorted(list_of_rating_obj, key=lambda x: x.date, reverse=True)

        print(self.database.get_hotel_obj(hotel_id))
        self.print_rating(list_of_rating_obj)




