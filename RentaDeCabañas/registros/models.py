from django.db import models
from ckeditor.fields import RichTextField 

class Cabañas(models.Model): #Define la estructura de nuestra tabla
    nombre= models.TextField()
    clave = models.CharField(primary_key=True,max_length=10)
    costoDia= models.IntegerField(verbose_name="Costo Por Día")
    numPersonas= models.TextField(verbose_name="Número De Personas Por Cabaña")
    numCamas= models.TextField(verbose_name="Número De Camas")
    servicios = models.TextField()
    imagen = models.ImageField(null=True, upload_to="fotos",verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Cabaña"
        verbose_name_plural="Cabañas"
        ordering=["-created"]

    def __str__(self):
        return self.nombre

class Promociones(models.Model): #Define la estructura de nuestra tabla
    validez= models.TextField()
    nombre = models.TextField()
    promo = models.TextField()
    imagen = models.ImageField(null=True, upload_to="fotos",verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Promoción"
        verbose_name_plural="Promociones"
        ordering=["-created"]

    def __str__(self):
        return self.validez

class Reservacion(models.Model): #Define la estructura de nuestra tabla
    cliente= models.TextField()
    numHu= models.TextField()
    fllegada= models.DateTimeField()
    fsalida= models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Reservacion"
        verbose_name_plural="Reservaciones"
        ordering=["-created"]

    def __str__(self):
        return self.cliente


