from django.shortcuts import render, redirect
from django.contrib import messages


# ===============================/ Página inicial Home /======================== #
def home(request):
    return render(request, 'home.html')  # Página de inicio

# ===============================/ Página Sobre Nosotros /======================== #
def aboutUs(request):
    return render(request, 'aboutUs.html')  # Página Sobre Nosotros

# ===============================/ Página Contáctanos /======================== #
def contactUs(request):
    return render(request, 'contactUs.html')  # Página de Contacto

# ===============================/ Página Servicios /======================== #
def services(request):
    return render(request, 'services.html')  # Página de Servicios