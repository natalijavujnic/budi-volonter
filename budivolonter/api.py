from django.urls import path
from .api_func import fetch_activities_org,update_free_spaces,fetch_activities_vol, resolveApplication, download

urlpatterns = [
    path('get_activities_org',fetch_activities_org),
    path('get_activities_vol',fetch_activities_vol),
    path('update_free_spaces',update_free_spaces),
    path('resolve_application',resolveApplication),
    path('download',download)
]
