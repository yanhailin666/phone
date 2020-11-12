from django.contrib import admin
from django.urls import path, re_path,include
from .views import *


urlpatterns = [
    path('information',information),
    path('china',china),
    path('overseas',overseas),
    path('add_gps_position',add_gps_position),
    path('update_gps_position',update_gps_position)
]