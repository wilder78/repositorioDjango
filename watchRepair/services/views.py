from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomerForm


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

# ===============================/ Página Servicios /======================== #
def register_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el cliente en la base de datos
            messages.success(request, "Cliente registrado con éxito.")  # Mensaje de éxito
            return redirect('home')  # Asegúrate de que 'home' está en urls.py
        else:
            messages.error(request, "Hubo un error en el formulario. Verifica los datos ingresados.")  # Mensaje de error
    else:
        form = CustomerForm()  # Si no es POST, renderiza el formulario vacío

    return render(request, 'register_customer.html', {'form': form})
