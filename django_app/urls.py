
from django.contrib import admin
from django.urls import path

from django_app import views

app_name = "django_app"

urlpatterns = [
    path("", views.main, name="main"),
    ]
