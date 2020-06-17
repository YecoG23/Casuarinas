from django.db import models
from django.contrib.gis.db import models as gismodels
from django.urls import reverse
from datetime import datetime
# Create your models here.

TIPOS_PAVIMENTOS = [
    ("SP", "Sin Pavimento"),
    ("PR", "Pavimento Rigido"),
    ("PA", "Pavimento Asfaltico"),
    ("GCS", "Graderia de concreto simple"),
    ("GCC", "Graderia de concreto ciclopeo"),
    ("VEREDA", "Vereda"),
]

TIPOS_EXCAVACION = [
    ("MAQUINARIA", "Maquinaria"),
    ("PULSO", "Pulso"),

]


TIPOS_SUELO = [
    ("TN", "Terreno Normal"),
    ("TSR", "Terreno Semirocoso"),
    ("TRF", "Terreno Rocoso Fracturado"),
    ("TM", "Terreno Mixto"),
    ("TR", "Terreno Rocoso"),

]

TIPOS_BUZON = [
    ("TIPO1", "Buzon Tipo 1"),
    ("TIPO2", "Buzon Tipo 2"),
    ("TIPO3", "Buzon Tipo 3"),
    ("NORMAL", "Buzon Normal"),

]

TIPOS_MAT_TUBERIA = [
    ("PVC-SN2", "Tuberia PVC SN2"),
    ("PVC-SN4", "Tuberia PVC SN4"),
    ("HDPE-SDR17", "Tuberia HDPE SDR17"),

]


class Buzon (gismodels.Model):
# LOS BUZONES TIENEN LAS SIGUIENTES PROPIEDADES
# NUMERO DE BUZON: BZ-01
# EJECUTADO?: SI O NO 
# PROFUNDIDAD: NUMERO ENTERO
# TIPO DE PAVIMENTO: PA, PR, SP
# TIPO DE EXCAVACION: MAQUINARIA O PULSO
# TIPO DE SUELO: TN, TSR, TR 
# DIAMETRO INTERNO: 1.2 BUZON TIPO 1 (EXISTE TIPO 2, TIPO 3, TIPO NORMAL)
	# DATOS PROPIOS DEL BUZON
	codigo = models.IntegerField(blank=True, null=True)
	ejecutado = models.CharField(max_length=100,blank=True)
	profundidad = models.FloatField(blank=True, null=True)
	tipo_pavimento = models.CharField(max_length=100, choices=TIPOS_PAVIMENTOS,blank=True)
	tipo_excavacion = models.CharField(max_length=100, choices=TIPOS_EXCAVACION,blank=True)
	tipo_suelo = models.CharField(max_length=100, choices=TIPOS_SUELO,blank=True)
	tipo_buzon = models.CharField(max_length=100, choices=TIPOS_BUZON,blank=True)
	#CAMPOS PARA CONTROL
	creado_en = models.DateTimeField(auto_now_add=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	# DATOS GEOGRAFICOS
	geom = gismodels.PointField(srid=4326)
	
	def __str__(self):
		return 'BZ-{0}'.format(self.codigo)

	# def get_absolute_url(self):
	# 	return reverse('update_buzon', kwargs={'pk': self.pk})

class RedSecundaria (gismodels.Model):
	# DATOS PROPIOS DE LA RED
	# codigo = models.IntegerField()
	nombre_habilitacion = models.CharField(max_length=100) #asentamiento humano, residencial, etc.
	nombre_pasaje_calle = models.CharField(max_length=100)

	buzon_aguas_arriba = models.CharField(max_length=100)
	buzon_aguas_abajo = models.CharField(max_length=100)

	profundidad_aguas_arriba = models.FloatField()
	profundidad_aguas_abajo = models.FloatField()

	tipo_pavimento = models.CharField(max_length=100, choices=TIPOS_PAVIMENTOS)
	tipo_excavacion = models.CharField(max_length=100, choices=TIPOS_EXCAVACION)
	longitud_horizontal = models.FloatField()
	pendiente = models.FloatField()
	longitud_real = models.FloatField()
	longitud_excavacion = models.FloatField()
	tipo_suelo = models.CharField(max_length=100, choices=TIPOS_SUELO)
	longitud_tuberia = models.FloatField()
	material_tuberia = models.CharField(max_length=100, choices=TIPOS_MAT_TUBERIA)
	DN_tuberia = models.PositiveIntegerField()

	#CAMPOS PARA CONTROL
	creado_en = models.DateTimeField(auto_now_add=True)
	actualizado_en = models.DateTimeField(auto_now=True)
	# DATOS GEOGRAFICOS
	geom = gismodels.LineStringField()

	def __str__(self):
		return 'RS-{00}'.format(self.pk)

	# def get_absolute_url(self):
	# 	return reverse('update_buzon', kwargs={'pk': self.pk})