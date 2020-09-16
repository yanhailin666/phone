from django.contrib import admin
from django.urls import path, re_path,include
from .views import *


urlpatterns = [
    path('information',information),
    path('china',china),
    path('overseas',overseas)
]