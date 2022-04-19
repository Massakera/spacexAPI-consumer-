from django.urls import path

from .views import launches


urlpatterns = [
    path('launches', launches, name = "launches"),
]