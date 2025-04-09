from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomerForm, EmployeeForm, SupplierForm, MechanicalWatchForm, QuartzWatchForm, SmartWatchForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Employee, Customer, Supplier, MechanicalWatch, QuartzWatch, SmartWatch
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

# ===============================/ Metodos Get para modificar o actualizar clientes /======================== #
@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail_api(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response({'error': 'Empleado no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response({'mensaje': 'Empleado eliminado'}, status=status.HTTP_204_NO_CONTENT)

# ===============================/ Metodos Get para modificar o actualizar clientes /======================== #
@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail_api(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return Response({'mensaje': 'Cliente eliminado'}, status=status.HTTP_204_NO_CONTENT)


# ===============================/ Metodos Get para modificar o actualizar Proveedores /======================== #
@api_view(['GET', 'PUT', 'DELETE'])
def supplier_detail_api(request, pk):
    try:
        supplier = Supplier.objects.get(pk=pk)
    except Supplier.DoesNotExist:
        return Response({'error': 'Proveedor no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SupplierSerializer(supplier)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SupplierSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        supplier.delete()
        return Response({'mensaje': 'Proveedor eliminado'}, status=status.HTTP_204_NO_CONTENT)


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

