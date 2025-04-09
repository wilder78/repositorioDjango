from . import views
from django.urls import path
from django.shortcuts import render
from .views import empleados_api, suppliers_api, customers_api, register_mechanical_watch, register_quartz_watch, register_smart_watch
from .views import supplier_detail_api, customer_detail_api, employee_detail_api


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
    path('suppliers/register/', views.register_supplier, name='register_supplier'),

    #  Modificar o actualizar clientes, empleados y proveedores.
    path('api/empleados/<int:pk>/', employee_detail_api, name='employee_detail_api'),
    path('api/clientes/<int:pk>/', customer_detail_api, name='customer_detail_api'),
    path('api/proveedores/<int:pk>/', supplier_detail_api, name='supplier_detail_api'),


    # Registrar los tipos de reloj 
    path('registrar-reloj/', register_mechanical_watch, name='register_mechanical_watch'),
    path('registrar-reloj-cuarzo/', register_quartz_watch, name='register_quartz_watch'),
    path('registrar-smartwatch/', register_smart_watch, name='register_smart_watch'),
    path('exito/', lambda request: render(request, 'success.html'), name='watch_success'),

    # Endpoints API
    # Llamado modo API a los personas.
    path('api/empleados/', empleados_api, name='empleados_api'),
    path('api/clientes/', customers_api, name='customers_api'),
    path('api/proveedores/', suppliers_api, name='suppliers_api'),

    # Llamado modo API a los relojes.
    path('api/relojes/mecanicos/', views.get_mechanical_watches, name='get_mechanical_watches'),
    path('api/relojes/cuarzo/', views.get_quartz_watches, name='get_quartz_watches'),
    path('api/relojes/inteligentes/', views.get_smart_watches, name='get_smart_watches'),
]


















