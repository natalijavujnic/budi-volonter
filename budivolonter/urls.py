
from django.contrib import admin
from django.urls import path
from .views import welcome,open_activity,reg_org, reg_vol, display_my_profile


urlpatterns = [
    path('welcome',welcome),
    path('open_activity',open_activity),
    path('register_organization',reg_org),
    path('register_volunteer', reg_vol),
    path('my_profile',display_my_profile)
]
