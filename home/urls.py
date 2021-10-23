from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    # Empty path shows its root url
    path('', views.index, name='home')
]
