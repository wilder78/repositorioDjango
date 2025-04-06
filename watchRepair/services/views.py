from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomerForm, EmployeeForm, MechanicalWatchForm, QuartzWatchForm, SmartWatchForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MechanicalWatch, QuartzWatch, SmartWatch
from .serializers import MechanicalWatchSerializer, QuartzWatchSerializer, SmartWatchSerializer



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


# ===============================/ Página clientes /======================== #
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


# ===============================/ Página registrar empleados /======================== #
def register_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el empleado en la base de datos
            return redirect('home')  # Redirige a la página de inicio o éxito
    else:
        form = EmployeeForm()  # Si no es POST, renderiza el formulario vacío

    return render(request, 'register_employee.html', {'form': form})


# ===============================/ Página registrar proveedores /======================== #
from django.shortcuts import render, redirect
from .forms import SupplierForm

def register_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el proveedor en la base de datos
            return redirect('home')  # Redirige a la página de inicio o éxito
    else:
        form = SupplierForm()  # Si no es POST, renderiza el formulario vacío

    return render(request, 'register_supplier.html', {'form': form})


# ===============================/ Página registrar relojes /======================== #

def register_watch(request):
    """Vista para registrar un reloj de cualquier tipo."""
    if request.method == 'POST':
        watch_type = request.POST.get('watch_type')  # Obtiene el tipo de reloj seleccionado

        # Selecciona el formulario adecuado según el tipo de reloj
        if watch_type == 'mechanical':
            form = MechanicalWatchForm(request.POST)
        elif watch_type == 'quartz':
            form = QuartzWatchForm(request.POST)
        elif watch_type == 'smart':
            form = SmartWatchForm(request.POST)
        else:
            form = None

        if form and form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página principal después del registro

    else:
        # Si es una solicitud GET, se crean formularios vacíos para cada tipo de reloj
        mechanical_form = MechanicalWatchForm()
        quartz_form = QuartzWatchForm()
        smart_form = SmartWatchForm()

    return render(request, 'register_watch.html', {
        'mechanical_form': mechanical_form,
        'quartz_form': quartz_form,
        'smart_form': smart_form
    })


# ===============================/ Metodos API de los modelos /======================== #
# Obtener todos los relojes mecánicos
@api_view(['GET'])
def get_mechanical_watches(request):
    watches = MechanicalWatch.objects.all()
    serializer = MechanicalWatchSerializer(watches, many=True)
    return Response(serializer.data)

# Obtener todos los relojes de cuarzo
@api_view(['GET'])
def get_quartz_watches(request):
    watches = QuartzWatch.objects.all()
    serializer = QuartzWatchSerializer(watches, many=True)
    return Response(serializer.data)

# Obtener todos los relojes inteligentes
@api_view(['GET'])
def get_smart_watches(request):
    watches = SmartWatch.objects.all()
    serializer = SmartWatchSerializer(watches, many=True)
    return Response(serializer.data)

