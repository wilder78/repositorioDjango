"""
URL configuration for watchRepair project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
<<<<<<< HEAD
from django.urls import path
from services.views import home, aboutUs, contactUs, services, register_customer, register_employee, register_watch, register_supplier  # Importamos las nuevas vistas

urlpatterns = [
    path('', home, name='home'),
    path('aboutUs/', aboutUs, name='aboutUs'),
    path('contactUs/', contactUs, name='contactUs'),
    path('services/', services, name='services'),
    path('register_customer/', register_customer, name='register_customer'),
    path('register_employee/', register_employee, name='register_employee'),
    path("register_watch/", register_watch, name="register_watch"),  # Ruta para registrar relojes
    path('register_supplier/', register_supplier, name='register_supplier'),
=======
from django.urls import path, include

urlpatterns = [
>>>>>>> part-01
    path('admin/', admin.site.urls),
    path('', include('services.urls')),  #  Esto enlaza todas las rutas de tu app
]



<<<<<<< HEAD
=======


>>>>>>> part-01
