from django.urls import path
from .api_func import fetch_activities
urlpatterns = [
    path('get_activities',fetch_activities)
]
