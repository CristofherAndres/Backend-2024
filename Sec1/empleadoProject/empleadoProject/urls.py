"""
URL configuration for empleadoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from empleadoApp.views import pruebaTemplate, tienda, jugueteria, electronica

urlpatterns = [
    path('admin/', admin.site.urls),
    path('template/', pruebaTemplate),
    path('tienda/', tienda, name='tienda'),
    path('jugueteria/', jugueteria, name='jugueteria'),
    path('electronica/', electronica, name='electronica'),
]
