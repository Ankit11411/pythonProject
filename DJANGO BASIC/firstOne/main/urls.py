from django.contrib import admin
from django.urls import path
# from .views import display, home
from . import views

urlpatterns = [
    path('<str:name>', views.display, name = 'display'),
    path('home/', views.home, name = 'home'),
]
