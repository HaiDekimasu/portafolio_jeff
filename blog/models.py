from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField( max_length=100)
    description = models.CharField(max_length=1000)
    habilit = models.CharField(max_length=250)
    image = models.ImageField( upload_to='blog/images')
    
    def __str__(self):
        return self.title
    

    