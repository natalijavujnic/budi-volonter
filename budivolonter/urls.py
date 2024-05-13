
from django.contrib import admin
from django.urls import path
from .views import welcome,open_activity,display_my_profile

urlpatterns = [
    path('',welcome),
    path('open_activity',open_activity),
    path('my_profile',display_my_profile)
]
