from django.urls import path
from .views import register_mechanical_watch, register_quartz_watch, register_smart_watch
from django.shortcuts import render
from . import views

urlpatterns = [
    # Páginas HTML
    path('', views.home, name='home'),
    # En services/urls.py
    path('about/', views.aboutUs, name='aboutUs'), 
    path('contact/', views.contactUs, name='contactUs'),
    path('services/', views.services, name='services'),

    #  Registrar clientes, empleados y proveedores
    path('clientes/registrar/', views.register_customer, name='register_customer'),
    path('empleados/registrar/', views.register_employee, name='register_employee'),

    # Registrar los tipos de reloj 
    path('registrar-reloj/', register_mechanical_watch, name='register_mechanical_watch'),
    path('registrar-reloj-cuarzo/', register_quartz_watch, name='register_quartz_watch'),
    path('registrar-smartwatch/', register_smart_watch, name='register_smart_watch'),
    path('exito/', lambda request: render(request, 'success.html'), name='watch_success'),

    # Endpoints API
    path('api/relojes/mecanicos/', views.get_mechanical_watches, name='get_mechanical_watches'),
    path('api/relojes/cuarzo/', views.get_quartz_watches, name='get_quartz_watches'),
    path('api/relojes/inteligentes/', views.get_smart_watches, name='get_smart_watches'),
]





