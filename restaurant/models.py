from django.db import models
#import default user model
from django.contrib.auth.models import User 
# Create your models here.

# Restaurant 


class Restaurant(models.Model):
    
    class TypeChoices(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        CHINESE = 'CH', 'Chinese'
        ITALIAN = 'IT', 'Italian'
        GREEK = 'GR', 'Greek'
        MEXICAN = 'MX', 'Mexican'
        FASTFOOD = 'FF', 'Fast Food'
        OTHER = 'OT', 'Other'

    def __str__(self):
        return f"Rating: {self.rating}"

    name = models.CharField(max_length=100)
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    restaurant_type = models.CharField(max_length=2, choices=TypeChoices.choices)

    def __str__(self):
        return self.name
    

# user

# Rating    
    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    def __str__(self):
        return f"Rating: {self.rating}"
    

class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, related_name='sales')
    #change in case of deletion ie. the value will be empty null=True
    income = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField()


#signals practice check test sync with user 
class Type_of_Business (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Type of business: {self.name}"

class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    username = models.CharField(max_length=150, unique=False, blank=False)
    email = models.EmailField(max_length=150, blank=False)
    location = models.CharField(max_length=150, blank=False)
    website = models.URLField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    company_name = models.CharField(max_length=200, blank=True)
    is_a_business = models.BooleanField(default=False)
    business = models.ForeignKey(Type_of_Business, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"username: {self.username}"