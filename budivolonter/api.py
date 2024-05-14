from django.urls import path
from .api_func import fetch_activities,update_free_spaces
urlpatterns = [
    path('get_activities',fetch_activities),
    path('update_free_spaces',update_free_spaces)
]
