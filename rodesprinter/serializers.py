from .models import User, Amenity, BookAmenity
from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):
    BookedAmenity = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('pk', 'name', 'location', 'BookedAmenity')

class AmenitySerializers(serializers.ModelSerializer):
    amenity  = serializers.PrimaryKeyRelatedField(many= True, read_only=True)
    class Meta:
        model = Amenity
        fields = ('pk', 'name', 'location','amenity')

class BookAmenitySerializers(serializers.ModelSerializer):
    amenity = serializers.PrimaryKeyRelatedField(queryset = Amenity.objects.all(), many=False)
    user = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), many=False)
    class Meta:
        model = BookAmenity
        fields = ('pk', 'amenity', 'user')