from django import forms
from .models import Contacto

class Contactoform(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'