# LLD_Hotel_Rating


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
