from restaurant.models import Restaurant, Rating, Sale
from django.utils import timezone

def run ():
    #instantiate the model
    restaurant = Restaurant()
    restaurant.name = 'Vivaldi'
    restaurant.latitude = 50.5
    restaurant.longitude = 50.2
    restaurant.date_opened = timezone.now()
    restaurant.restaurant_type = Restaurant.TypeChoices.ITALIAN
    restaurant.save()
