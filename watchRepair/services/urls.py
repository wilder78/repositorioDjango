from django.urls import path
from . import views

urlpatterns = [
    # Páginas HTML
    path('', views.home, name='home'),
    # En services/urls.py
    path('about/', views.aboutUs, name='aboutUs'), 
    path('contact/', views.contactUs, name='contactUs'),
    path('services/', views.services, name='services'),
    path('clientes/registrar/', views.register_customer, name='register_customer'),
    path('empleados/registrar/', views.register_employee, name='register_employee'),
    path('relojes/registrar/', views.register_watch, name='register_watch'),

    # Endpoints API
    path('api/relojes/mecanicos/', views.get_mechanical_watches, name='get_mechanical_watches'),
    path('api/relojes/cuarzo/', views.get_quartz_watches, name='get_quartz_watches'),
    path('api/relojes/inteligentes/', views.get_smart_watches, name='get_smart_watches'),
]
