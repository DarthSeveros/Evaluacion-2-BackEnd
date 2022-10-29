from restaurant import settings
from django.db import models

# Create your models here.

class Reservas(models.Model):
    RESERVAS_OPTIONS = (
        ('Reservado', 'RESERVADO'),
        ('Completado', 'COMPLETADA'), 
        ('Anulada', 'ANULADA'), 
        ('No Asisten', 'NO ASISTEN')
    )

    nombre_persona = models.CharField(max_length=60)
    telefono = models.CharField(max_length=20)
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    cantidad_personas = models.IntegerField()
    estado_reserva = models.CharField(max_length=10, choices=RESERVAS_OPTIONS)
    observacion = models.CharField(max_length=120, blank=True)