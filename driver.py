"""
MAIN FUNCTION
"""
from database.Database import Database
from models.Hotel import Hotel
from models.Rating import Rating
from models.User import User
from service.Service import Service

# Database
db: Database = Database()

# Service
service = Service(db)

# Users
user1 = User("Jitesh")
user2 = User("Tarun")
user3 = User("Sumit")
user4 = User("Priyanka")

db.add_user_to_database(user1)
db.add_user_to_database(user2)
db.add_user_to_database(user3)
db.add_user_to_database(user4)

# Hotel
hotel1 = Hotel("Radisson", True)
hotel2 = Hotel("LeelaPalace")
hotel3 = Hotel("TwoStar")
hotel4 = Hotel("Taj", True)
hotel5 = Hotel("Oberoi")
hotel6 = Hotel("SandPiper")

db.add_hotel_to_database(hotel1)
db.add_hotel_to_database(hotel2)
db.add_hotel_to_database(hotel3)
db.add_hotel_to_database(hotel4)
db.add_hotel_to_database(hotel5)
db.add_hotel_to_database(hotel6)

# Rating
rating1 = Rating(user1.get_id(), hotel1.get_id(), 4, "Good Nice Place")
rating2 = Rating(user2.get_id(), hotel1.get_id(), 1, "Bad Place")
rating3 = Rating(user3.get_id(), hotel1.get_id(), 2, "Water Not Working")
rating4 = Rating(user4.get_id(), hotel1.get_id(), 1, "Geyser Not working")
rating5 = Rating(user1.get_id(), hotel3.get_id(), 5, "Good Nice Place")
rating6 = Rating(user1.get_id(), hotel5.get_id(), 5, "Best Place to Stay")
rating7 = Rating(user3.get_id(), hotel6.get_id(), 2, "Manager bad talking")
rating8 = Rating(user2.get_id(), hotel3.get_id(), 3, "No Parking")

db.add_rating_to_database(rating1)
db.add_rating_to_database(rating2)
db.add_rating_to_database(rating3)
db.add_rating_to_database(rating4)
db.add_rating_to_database(rating5)
db.add_rating_to_database(rating6)
db.add_rating_to_database(rating7)
db.add_rating_to_database(rating8)

# Queries
service.find_all_hotels()
print()
service.find_all_hotels(_filter=1, _order="DESC")
print()
service.find_all_ratings(hotel1.get_id(), _filter=1, _order="DESC")
print()
service.find_all_ratings(hotel3.get_id())
