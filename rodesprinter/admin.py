from django.contrib import admin
from .models import User, Amenity, BookAmenity
# Register your models here.
admin.site.register(User)
admin.site.register(Amenity)
admin.site.register(BookAmenity)