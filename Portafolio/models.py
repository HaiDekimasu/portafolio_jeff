from django.db import models

# Create your models here.
class Projecto(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField( max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="Portafolio/images/")
    url =models.URLField(blank=True)
    
    def __str__(self) -> str:
        return self.title
    
class Presentacion(models.Model):
    image = models.ImageField(upload_to="Portafolio/images/")
    title = models.CharField( max_length=100)
    description = models.CharField(max_length=250)
    id = models.AutoField(primary_key=True)
    
    
    def __str__(self) -> str:
        return self.title
    
    
class Imgpresent(models.Model):
    imagen = models.ImageField(upload_to='Portafolio/images')
    title = models.CharField( max_length=100)
    id = models.AutoField(primary_key=True)
    
    def __str__(self)-> str:
        return self.title