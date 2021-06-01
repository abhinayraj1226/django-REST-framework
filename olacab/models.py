from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=20)
    status = models.BooleanField()
    rate = models.IntegerField() # rate per unit/KM.
    latitude = models.IntegerField()
    longitude = models.IntegerField()

    def __str__(self):
        return self.name+"id: "+str(self.pk)    

class BookRides(models.Model):
    name = models.CharField(max_length = 20)
    latitude = models.IntegerField()
    longitude = models.IntegerField()

    def __str__(self):
        return self.name+"id: "+str(self.pk)
