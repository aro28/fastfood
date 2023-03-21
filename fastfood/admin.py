from django.contrib import admin
from .models import Order, Food, Ingredient
# Register your models here.
admin.site.register(Order)
admin.site.register(Food)
admin.site.register(Ingredient)