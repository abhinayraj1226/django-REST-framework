from . import views
from django.urls import path

urlpatterns = [
    path('restaurant', views.restaurant, name="restaurant"),
    path('cuisine', views.cuisine, name="cuisine"),
    path('user', views.user, name="user"),
    path('search', views.searchrestaurant, name="searchrestaurant"),
    path('bookRestaurant', views.bookRestaurant, name="bookRestaurant")
]
