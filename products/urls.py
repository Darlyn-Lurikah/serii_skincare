from django.urls import path
from . import views

urlpatterns = [

    # Empty path shows its root url
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail')
]