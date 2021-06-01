from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

category_choices = ( ('VEG','VEG'), ('NON-VEG', 'NON-VEG')   )


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length = 50)

    def __str__(self):
        return str(self.pk)

class User(models.Model):
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)

    def __str__(self):
        return str(self.pk)


class Cuisine(models.Model):
    name = models.CharField(max_length = 50)
    category = models.CharField(max_length = 10, choices=category_choices, default='VEG')
    restaurant = models.ForeignKey(Restaurant, related_name="cuisine", on_delete=CASCADE)

    def __str__(self):
        return str(self.pk)



class BookRestaurent(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name="book_restaurant", on_delete=CASCADE)
    user = models.ForeignKey(User, related_name="book_restaurant", on_delete=CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)



