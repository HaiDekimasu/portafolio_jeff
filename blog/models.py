from django.db import models
import datetime

# Create your models here.
class post(models.Model):
    title = models.CharField( max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField( upload_to='blog/images')
    date = models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return self.title
    
    