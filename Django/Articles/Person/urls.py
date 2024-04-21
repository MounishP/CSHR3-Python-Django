from django.urls import path
from Person.views import home

urlpatterns = [
    path('', home, name="home"),
]
