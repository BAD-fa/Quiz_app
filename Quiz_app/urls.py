from django.contrib import admin
from django.urls import path

from .views import create_quiz

urlpatterns = [
    path('<str:username>/', create_quiz),
]