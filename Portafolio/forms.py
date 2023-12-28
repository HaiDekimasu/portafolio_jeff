from django import forms
from .models import Contacto

class Contactoform(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    correo = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control"}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
    class Meta:
        model = Contacto
        fields = '__all__'