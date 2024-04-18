from django.urls import path
from .views import homepage,about,cars

urlpatterns = [
    path('',homepage,name="homepage"),
    path('about/',about,name="about"),
    path('cars/',cars)  
]