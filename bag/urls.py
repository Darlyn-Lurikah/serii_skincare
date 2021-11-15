from django.urls import path
from . import views

urlpatterns = [

    # Empty path shows its root url
    path('', views.view_bag, name='view_bag')
]