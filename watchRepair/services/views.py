from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomerForm, EmployeeForm, SupplierForm, MechanicalWatchForm, QuartzWatchForm, SmartWatchForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Supplier, MechanicalWatch, QuartzWatch, SmartWatch
from .serializers import Employee, CustomerSerializer, EmployeeSerializer, SupplierSerializer, MechanicalWatchSerializer, QuartzWatchSerializer, SmartWatchSerializer


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


# ===============================/ Página registrar clientes /======================== #
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
# Reloj mecanico.
def register_mechanical_watch(request):
    if request.method == 'POST':
        form = MechanicalWatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('watch_success')  # Ruta de éxito
    else:
        form = MechanicalWatchForm()

    return render(request, 'register_mechanical_watch.html', {'form': form})

# Reloj de cuarzo.
def register_quartz_watch(request):
    if request.method == 'POST':
        form = QuartzWatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('watch_success')  # Ruta de éxito después del registro
    else:
        form = QuartzWatchForm()
    
    return render(request, 'register_quartz_watch.html', {'form': form})

# Smart watch.
def register_smart_watch(request):
    if request.method == 'POST':
        form = SmartWatchForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Smartwatch registrado exitosamente.")
            return redirect('register_smart_watch')  # Vuelve al mismo formulario limpio
    else:
        form = SmartWatchForm()
    
    return render(request, 'register_smart_watch.html', {'form': form})

# Salida
def watch_success_view(request):
    return render(request, 'success.html')

# ===============================/ Metodos API de los modelos de Personas /======================== #
# Obtener los empleados.
@api_view(['GET'])
def empleados_api(request):
    empleados = Employee.objects.all()
    serializer = EmployeeSerializer(empleados, many=True)
    return Response(serializer.data)

# Obtener los clientes.
@api_view(['GET'])
def customers_api(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)

# Obtener los proveedores.
@api_view(['GET'])
def suppliers_api(request):
    suppliers = Supplier.objects.all()
    serializer = SupplierSerializer(suppliers, many=True)
    return Response(serializer.data)


# ===============================/ Metodos API de los modelos de relojes /======================== #
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

