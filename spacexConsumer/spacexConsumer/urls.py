"""spacexConsumer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import launches, launch_sites, launches_2019_2021

urlpatterns = [
    path('admin/', admin.site.urls),
    path('launches/total', launches, name = "launches"),
    path('launches/sites', launch_sites, name="launch_sites"),
    path('launches/start=2019&end=2021', launches_2019_2021, name='launches_2019_2021')
]
