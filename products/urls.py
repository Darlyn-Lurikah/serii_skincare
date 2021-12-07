from django.urls import path
from . import views

urlpatterns = [
    # Empty path shows its root url
    path('', views.all_products, name='products'),
    # Ensure product id comes as an integer not string
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
]
