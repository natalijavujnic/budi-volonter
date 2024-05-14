from django.contrib import admin
from django.urls import path,include
from .views import welcome, open_activity, reg_org, reg_vol, display_my_profile, login_page, do_logout

urlpatterns = [
    path('welcome',welcome, name='welcome'),
    path('open_activity',open_activity, name='open_activity'),
    path('register_organization',reg_org, name='register_organization'),
    path('register_volunteer', reg_vol, name='register_volunteer'),
    path('my_profile',display_my_profile, name='my_profile'),
    path('login', login_page, name='login'),
    path('logout', do_logout, name='logout'),
    path('api/',include('budivolonter.api'))
]
