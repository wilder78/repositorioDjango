from django.db import models
from django.utils import timezone


# ========================/ Base models for watches. /========================= #
class Watch(models.Model):
    brand = models.CharField(max_length=100)
    type_of_machinery = models.CharField(max_length=50)
    model = models.CharField(max_length=100)

    class Meta:
        abstract = True  # Modelo abstracto para evitar crear tabla en la BD

    def general_maintenance(self, extra_info=""):
        return f"Mantenimiento realizado en el reloj {self.brand} {self.model} ({self.type_of_machinery}). {extra_info}"

    def get_information(self):
        return f"{self.brand} {self.model} - Tipo: {self.type_of_machinery}" 

    def __str__(self):
        return self.get_information()

    @classmethod
    def get_by_brand(cls, brand):
        """Obtiene todos los relojes de una marca específica"""
        return cls.objects.filter(brand=brand)

# ===========================/ Clases hijas de Watch /=========================== #
class MechanicalWatch(Watch):
    WINDING_CHOICES = [("manual", "Manual"), ("automatic", "Automático")]
    winding_type = models.CharField(max_length=10, choices=WINDING_CHOICES, default="manual")

    def general_maintenance(self):
        return f"Se ha realizado calibración ({self.winding_type}), limpieza y lubricación en el reloj {self.brand} {self.model} ({self.type_of_machinery})."

    @classmethod
    def get_manual_winding_watches(cls):
        """Obtiene todos los relojes mecánicos de cuerda manual"""
        return cls.objects.filter(winding_type="manual")


class QuartzWatch(Watch):
    battery_life = models.IntegerField(default=2)  # Vida útil de la batería en años.

    def general_maintenance(self):
        return f"Se ha realizado limpieza y cambio de batería en el reloj {self.brand} {self.model} ({self.type_of_machinery})."

    @classmethod
    def get_watches_with_battery_life(cls, years):
        """Obtiene todos los relojes de cuarzo con una vida de batería mayor o igual a la indicada"""
        return cls.objects.filter(battery_life__gte=years)


class SmartWatch(Watch):
    os = models.CharField(max_length=50, default="Desconocido")  # Sistema operativo
    connectivity = models.CharField(max_length=100, default="No especificado")  # Tipos de conectividad

    def general_maintenance(self):
        return f"Se ha realizado actualización de software y revisión de sensores en el reloj {self.brand} {self.model} ({self.type_of_machinery})."

    @classmethod
    def get_by_os(cls, os_name):
        """Obtiene todos los relojes inteligentes con un sistema operativo específico"""
        return cls.objects.filter(os=os_name)

    class Meta:
        verbose_name = "Reloj Inteligente"
        verbose_name_plural = "Relojes Inteligentes"


# ========================/ Base models for person. /========================= #
class Person(models.Model):
    name = models.CharField(max_length=100)
    identification = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name} - ID: {self.identification} - Tel: {self.phone}"
    
    @classmethod
    def get_by_identification(cls, identification):
        """Obtiene una persona por su número de identificación."""
        return cls.objects.filter(identification=identification).first()
    
    @classmethod
    def exists_by_identification(cls, identification):
        """Verifica si existe una persona con la identificación dada."""
        return cls.objects.filter(identification=identification).exists()


# ===========================/ Clases hijas de Person /=========================== #
class Customer(Person):
    email = models.EmailField(unique=True)

    @classmethod
    def get_by_email(cls, email):
        """Busca un cliente por su correo electrónico."""
        return cls.objects.filter(email=email).first()


class Employee(Person):
    post = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    @classmethod
    def get_by_post(cls, post):
        """Obtiene todos los empleados con un determinado cargo."""
        return cls.objects.filter(post=post)


class Supplier(Person):
    company = models.CharField(max_length=100)
    products = models.TextField()

    @classmethod
    def get_by_company(cls, company_name):
        """Busca un proveedor por el nombre de su compañía."""
        return cls.objects.filter(company=company_name).first()


# ========================/ Modelo de Servicios corregido /========================= #
class Service(models.Model):
    mechanical_watch = models.ForeignKey(MechanicalWatch, on_delete=models.SET_NULL, null=True, blank=True)
    quartz_watch = models.ForeignKey(QuartzWatch, on_delete=models.SET_NULL, null=True, blank=True)
    smart_watch = models.ForeignKey(SmartWatch, on_delete=models.SET_NULL, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default="Pendiente")
    observations = models.TextField(blank=True, null=True)
    parts_used = models.TextField(blank=True, null=True)
    received_date = models.DateField(default=timezone.now)
    delivery_date = models.DateField(blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def complete_service(self):
        self.status = "Terminado"
        self.delivery_date = timezone.localdate()
        self.save()


