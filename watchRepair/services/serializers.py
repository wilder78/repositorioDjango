from rest_framework import serializers
from .models import Employee, Customer, Supplier, MechanicalWatch, QuartzWatch, SmartWatch




# ========================/ Serializador de las clases personas. /========================= #
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'



# ========================/ Serializador de las clases relojes. /========================= #
class MechanicalWatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MechanicalWatch
        fields = ['id', 'brand', 'type_of_machinery', 'model', 'winding_type']

class QuartzWatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuartzWatch
        fields = ['id', 'brand', 'type_of_machinery', 'model', 'battery_life']

class SmartWatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartWatch
        fields = ['id', 'brand', 'type_of_machinery', 'model', 'os', 'connectivity']



