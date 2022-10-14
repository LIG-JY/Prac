from django.urls import path  # import path function

from . import views  # same directory

urlpatterns = [
    path('', views.index),  # route, view
]