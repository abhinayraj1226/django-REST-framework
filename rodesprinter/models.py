from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Amenity(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length = 50)

    def __str__(self):
        return str(self.pk)

class User(models.Model):
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)

    def __str__(self):
        return str(self.pk)




class BookAmenity(models.Model):
    amenity = models.ForeignKey(Amenity, related_name="amenity", on_delete=CASCADE)
    user = models.ForeignKey(User, related_name="BookedAmenity", on_delete=CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)



