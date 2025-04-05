from rest_framework import serializers
from .models import MechanicalWatch, QuartzWatch, SmartWatch

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



# from rest_framework import serializers
# from .models import CustomerForm, EmployeeForm, MechanicalWatchForm, QuartzWatchForm, SmartWatchForm