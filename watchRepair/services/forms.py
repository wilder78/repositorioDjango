from django import forms
from .models import Customer

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

