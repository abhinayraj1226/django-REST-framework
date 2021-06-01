from . import views
from django.urls import path

urlpatterns = [
    path('amenity', views.amenity, name="amenity"),
    path('user', views.user, name="user"),
    path('search', views.searchAmenity, name="searchAmenity"),
    path('bookAmenity', views.bookAmenity, name="bookAmenity")
]
