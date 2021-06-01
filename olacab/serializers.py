from .models import Driver, BookRides
from rest_framework import serializers

class DriverSerializers(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('pk','name', 'status', 'rate', 'latitude', 'longitude')


class BookRidesSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookRides
        fields = ('pk','name','latitude', 'longitude')