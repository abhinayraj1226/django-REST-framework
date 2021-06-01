import re
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Driver, BookRides
from rest_framework import status
from .serializers import DriverSerializers, BookRidesSerializers
import math
# Create your views here.

@csrf_exempt
def driver(request):

    if request.method == "GET":
        driver = Driver.objects.all()

        driver_serializers = DriverSerializers(driver, many=True)
        return JsonResponse(driver_serializers.data, status=status.HTTP_200_OK, safe=False)
    elif request.method == "POST":
        driver = JSONParser().parse(request)

        driver_serializers = DriverSerializers(data = driver)
        if driver_serializers.is_valid():
            driver_serializers.save()
            return JsonResponse(driver_serializers.data, status=status.HTTP_202_ACCEPTED, safe=False)
        JsonResponse(driver_serializers.errors, status=status.HTTP_202_ACCEPTED)

@csrf_exempt
def bookRides(request):

    if request.method == "GET":
        rides = BookRides.objects.all()
        bookRides_serializers = BookRidesSerializers(rides, many=True)
        return JsonResponse(bookRides_serializers.data, status=status.HTTP_200_OK, safe=False)

    elif request.method == "POST":

        rides_data = JSONParser().parse(request)
        driver_data = Driver.objects.get(status=True)
        rides_detail = calculateTimeFare(rides_data, driver_data)

        bookRides_serializers = BookRidesSerializers(data = rides_data)
        if bookRides_serializers.is_valid():
            bookRides_serializers.save()
            return JsonResponse(rides_detail, status=status.HTTP_200_OK, safe=False)
        return JsonResponse(bookRides_serializers.errors, status=status.HTTP_200_OK, safe=False)
    


def calculateTimeFare(rides_data, driver_data):

    driver_lat = driver_data.latitude
    driver_long = driver_data.longitude

    rides_lat = rides_data['latitude']
    rides_long = rides_data['longitude']

    lat = math.fabs(driver_lat - rides_lat)
    long = math.fabs(driver_long - rides_long)

    ETA = (lat+long)/2

    fare = str(driver_data.rate * ETA)

    rides_detail = {
        "driver_name" : driver_data.name,
        "client_name" : rides_data['name'],
        "ETA" : str(ETA)+" min",
        "fare" : "Rs. "+fare
    }
    return rides_detail


