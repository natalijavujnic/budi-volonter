
from django.contrib import admin
from django.urls import path
from .views import welcome,open_activity

urlpatterns = [
    path('',welcome),
    path('open_activity',open_activity)
]
