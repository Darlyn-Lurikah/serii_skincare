from django.contrib import admin
from .models import Product, Category


# Controls fields displayed in admin panel (tuple)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image'
    )

    # Order products by sku 
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )

# Registering Product & Category models.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin) 