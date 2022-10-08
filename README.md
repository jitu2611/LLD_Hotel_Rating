# LLD_Hotel_Rating

user1 = User("Jitesh")
user2 = User("Tarun")
user3 = User("Sumit")
user4 = User("Priyanka")


hotel1 = Hotel("Radisson", True)
hotel2 = Hotel("LeelaPalace")
hotel3 = Hotel("TwoStar")
hotel4 = Hotel("Taj", True)
hotel5 = Hotel("Oberoi")
hotel6 = Hotel("SandPiper")

rating1 = Rating(user1.get_id(), hotel1.get_id(), 4, "Good Nice Place")
rating2 = Rating(user2.get_id(), hotel1.get_id(), 1, "Bad Place")
rating3 = Rating(user3.get_id(), hotel1.get_id(), 2, "Water Not Working")
rating4 = Rating(user4.get_id(), hotel1.get_id(), 1, "Geyser Not working")
rating5 = Rating(user1.get_id(), hotel3.get_id(), 5, "Good Nice Place")
rating6 = Rating(user1.get_id(), hotel5.get_id(), 5, "Best Place to Stay")
rating7 = Rating(user3.get_id(), hotel6.get_id(), 2, "Manager bad talking")
rating8 = Rating(user2.get_id(), hotel3.get_id(), 3, "No Parking")



# Queries
1) service.find_all_hotels()

Hotel(name='Radisson', rating=2.0, plus_size=True)
Hotel(name='Taj', rating=0, plus_size=True)
Hotel(name='LeelaPalace', rating=0, plus_size=0)
Hotel(name='TwoStar', rating=4.0, plus_size=0)
Hotel(name='Oberoi', rating=5.0, plus_size=0)
Hotel(name='SandPiper', rating=2.0, plus_size=0)

2) service.find_all_hotels(_filter=1, _order="DESC")

Hotel(name='Radisson', rating=2.0, plus_size=True)
Hotel(name='Oberoi', rating=5.0, plus_size=0)
Hotel(name='TwoStar', rating=4.0, plus_size=0)
Hotel(name='SandPiper', rating=2.0, plus_size=0)

3) service.find_all_ratings(hotel1.get_id(), _filter=1, _order="DESC")

Hotel(name='Radisson', rating=2.0, plus_size=True)
4, Good Nice Place, 2022-10-09 00:47:27.550593
2, Water Not Working, 2022-10-09 00:47:27.550619
1, Bad Place, 2022-10-09 00:47:27.550610
1, Geyser Not working, 2022-10-09 00:47:27.550626

4) service.find_all_ratings(hotel3.get_id())

Hotel(name='TwoStar', rating=4.0, plus_size=0)
3, No Parking, 2022-10-09 00:47:27.550656
5, Good Nice Place, 2022-10-09 00:47:27.550634
