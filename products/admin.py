from django.contrib import admin
from .models import Product, Category

# Registering Product & Category models.
admin.site.register(Product)
admin.site.register(Category)