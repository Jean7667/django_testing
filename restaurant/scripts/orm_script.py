from restaurant.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection


#fct to create a restaurant method save
""" def run ():
    #instantiate the model
    restaurant = Restaurant()
    restaurant.name = 'Vivaldi'
    restaurant.latitude = 50.5
    restaurant.longitude = 50.2
    restaurant.date_opened = timezone.now()
    restaurant.restaurant_type = Restaurant.TypeChoices.ITALIAN
    restaurant.save() """

#intro to manager (object)

""" def run():
    #query to get all the lines
    restaurants = Restaurant.objects.all()
    print(restaurants)
    print(connection.queries) """

# def run():
#     #query to get the first line
#     restaurants = Restaurant.objects.first()
#     print(restaurants)
#     print(connection.queries)

# def run():
#     #query to get all at index 0
#     restaurants = Restaurant.objects.all()[0]
#     print(restaurants)
#     print(connection.queries)


#fct to create a restaurant with create method
""" def run ():
    Restaurant.objects.create(
        name = 'Mazanoli',
        latitude = 45.3,
        longitude = 34.2,
        date_opened = timezone.now(),
        restaurant_type = Restaurant.TypeChoices.ITALIAN,
    )
    print(connection.queries) """
