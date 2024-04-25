from django.urls import path
from youtube.views import youtube

urlpatterns = [
    path('',youtube, name='youtube')
]
