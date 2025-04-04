from django import forms
from .models import MechanicalWatch, QuartzWatch, SmartWatch, Customer, Employee, Supplier

# ===============================/ Codigo formulario para registrar relojes /======================== #
class MechanicalWatchForm(forms.ModelForm):
    class Meta:
        model = MechanicalWatch
        fields = ['brand', 'model', 'type_of_machinery', 'winding_type']
        labels = {
            'brand': 'Marca',
            'model': 'Modelo',
            'type_of_machinery': 'Tipo de Maquinaria',
            'winding_type': 'Tipo de Cuerda'
        }

class QuartzWatchForm(forms.ModelForm):
    class Meta:
        model = QuartzWatch
        fields = ['brand', 'model', 'type_of_machinery', 'battery_life']
        labels = {
            'brand': 'Marca',
            'model': 'Modelo',
            'type_of_machinery': 'Tipo de Maquinaria',
            'battery_life': 'Vida Útil de la Batería (años)'
        }

class SmartWatchForm(forms.ModelForm):
    class Meta:
        model = SmartWatch
        fields = ['brand', 'model', 'type_of_machinery', 'os', 'connectivity']
        labels = {
            'brand': 'Marca',
            'model': 'Modelo',
            'type_of_machinery': 'Tipo de Maquinaria',
            'os': 'Sistema Operativo',
            'connectivity': 'Conectividad'
        }

# ===============================/ Codigo formulario para registrar clientes /======================== #
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'identification', 'phone', 'email']  # Campos correctos

    def clean_identification(self):
        """Verifica si la identificación ya existe en la base de datos."""
        identification = self.cleaned_data.get('identification')

        # Verifica si la identificación ya está registrada, excepto en el caso de edición
        if Customer.objects.filter(identification=identification).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Ya existe un cliente con esta identificación.")
        return identification


# ===============================/ Codigo formulario para registrar empleados /======================== #
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'identification', 'phone', 'post', 'salary']
        labels = {
            'name': 'Nombre Completo',
            'identification': 'Número de Identificación',
            'phone': 'Teléfono',
            'post': 'Cargo',
            'salary': 'Salario',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre completo'}),
            'identification': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la identificación'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el teléfono'}),
            'post': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el cargo'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el salario'}),
        }

    def clean_identification(self):
        """Verifica si la identificación ya existe en la base de datos."""
        identification = self.cleaned_data.get('identification')
        if Employee.objects.filter(identification=identification).exists():
            raise forms.ValidationError("Ya existe un empleado con esta identificación.")
        return identification

# ===============================/ Codigo formulario para registrar proveedor /======================== #
class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'identification', 'phone', 'company', 'products']  # Campos visibles en el formulario

    def clean_identification(self):
        """Verifica si la identificación ya existe en la base de datos."""
        identification = self.cleaned_data.get('identification')
        if Supplier.exists_by_identification(identification):
            raise forms.ValidationError("Ya existe un proveedor con esta identificación.")
        return identification

    def clean_company(self):
        """Verifica que el nombre de la empresa no esté vacío."""
        company = self.cleaned_data.get('company')
        if not company.strip():
            raise forms.ValidationError("El nombre de la empresa no puede estar vacío.")
        return company
