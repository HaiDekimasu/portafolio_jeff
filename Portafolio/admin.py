from django.contrib import admin
from .models import Projecto, Presentacion, Imgpresent, Contacto

# Register your models here.

admin.site.register(Projecto),
admin.site.register(Presentacion),
admin.site.register(Imgpresent),
admin.site.register(Contacto)

