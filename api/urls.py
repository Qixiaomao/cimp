from django.contrib import admin
from django.urls import path,include
from api import sign
from api.models import User


urlpatterns = [
    path('sign',sign.sign_or_out),
]
