from .models import Restaurant, Cuisine, User, BookRestaurent
from rest_framework import serializers
from datetime import date

class UserSerializers(serializers.ModelSerializer):
    book_restaurant = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('pk', 'name', 'location', 'book_restaurant')

class CuisineSerializers(serializers.ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(queryset = Restaurant.objects.all(), many=False)

    class Meta:
        model = Cuisine
        fields = ('pk', 'name', 'category', 'restaurant')

class RestaurantSerializers(serializers.ModelSerializer):
    book_restaurant = cuisine = serializers.PrimaryKeyRelatedField(many= True, read_only=True)
    # book_restaurant = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    class Meta:
        model = Restaurant
        fields = ('pk', 'name', 'location','book_restaurant', 'cuisine')

class BookRestaurentSerializers(serializers.ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(queryset = Restaurant.objects.all(), many=False)
    user = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), many=False)
    class Meta:
        model = BookRestaurent
        fields = ('pk', 'restaurant', 'user')