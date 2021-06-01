from . import views
from django.urls import path

urlpatterns = [
    path('driver', views.driver, name="driver"),
    path('rides', views.bookRides, name="bookRides"),
]
