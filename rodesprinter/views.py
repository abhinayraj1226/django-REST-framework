from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from .models import Amenity, User, BookAmenity
from .serializers import AmenitySerializers, UserSerializers, BookAmenitySerializers
from rest_framework.parsers import JSONParser
# Create your views here.


@csrf_exempt
def amenity(request):

    if request.method == "GET":
        restaurant = Amenity.objects.all()

        restaurant_serializers = AmenitySerializers(restaurant, many=True)
        return JsonResponse(restaurant_serializers.data, status=status.HTTP_200_OK, safe=False)
    
    elif request.method == "POST":
        restaurant_data = JSONParser().parse(request)

        restaurant_serializers = AmenitySerializers(data = restaurant_data)
        if restaurant_serializers.is_valid():
            restaurant_serializers.save()
            return JsonResponse(restaurant_serializers.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(restaurant_serializers.errors, status=status.HTTP_406_NOT_ACCEPTABLE, safe=False)

@csrf_exempt  
def user(request):

    if request.method == "GET":
        user = User.objects.all()

        user_serializers = UserSerializers(user, many = True)
        return JsonResponse(user_serializers.data, status=status.HTTP_200_OK, safe=False)

    elif request.method == "POST":
        user_data = JSONParser().parse(request)

        user_serializers = UserSerializers(data = user_data)

        if user_serializers.is_valid():
            user_serializers.save()
            return JsonResponse(user_serializers.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(user_serializers.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


@csrf_exempt
def bookAmenity(request):

    if request.method == "GET":
        bookRestaurent = BookAmenity.objects.all()

        bookRestaurent_serializers = BookAmenitySerializers(bookRestaurent, many = True)
        return JsonResponse(bookRestaurent_serializers.data, status=status.HTTP_200_OK, safe=False)
    
    elif request.method == "POST":
        bookRestaurent_data = JSONParser().parse(request)

        bookRestaurent_serializers = BookAmenitySerializers(data = bookRestaurent_data)

        if bookRestaurent_serializers.is_valid():
            bookRestaurent_serializers.save()
            return JsonResponse(bookRestaurent_serializers.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(bookRestaurent_serializers.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


@csrf_exempt
def searchAmenity(request):

    if request.method == "POST":
        search_data = JSONParser().parse(request)
        key_list = list(search_data.keys())

        attr = key_list[0]
        value = search_data[attr]

        my_filter={}
        my_filter[attr] = value
        restaurant = Amenity.objects.filter(**my_filter)

        restaurant_serializers = AmenitySerializers(restaurant, many = True)
        return JsonResponse(restaurant_serializers.data, status=status.HTTP_200_OK, safe=False)




        

