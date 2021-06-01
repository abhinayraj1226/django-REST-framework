from django.contrib import admin
from .models import Cuisine, Restaurant, BookRestaurent, User
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Cuisine)
admin.site.register(User)
admin.site.register(BookRestaurent)
