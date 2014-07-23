from django.db import models
'''
class Tipo(models.Model):
	nombre = models.CharField(max_length=10, unique=True)

	def __str__(self):
		return self.nombre
'''

class Device(models.Model):
	nombre = models.CharField(max_length=100, unique=True)
	ip = models.CharField(max_length=12, unique=True)
	estado = models.CharField(max_length=10)
	tipo = models.CharField(max_length=10, unique=True)
	#tipo = models.ForeignKey(Tipo, null=True)

	def __str__(self):
		return self.nombre


class Application(models.Model):
	nombre = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.nombre, self.estado


class deviceApp(models.Model):
	dispositivos = models.ForeignKey(Device)
	aplicaciones = models.ForeignKey(Application)
	estado = models.CharField(max_length=10)

	def __str__(self):
		return self.estado