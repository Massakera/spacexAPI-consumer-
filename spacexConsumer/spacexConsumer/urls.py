from django.contrib import admin
from django.urls import path
from main.views import launches, export_csv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', launches, name = "launches"),
    path('export/', export_csv, name='export')
]
