from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404 
from .models import Projecto, Presentacion
from .forms import Contactoform

# Create your views here.
# def vporfolio(request):
#     proyecto = Projecto.objects.all()
#     presentaciones = Presentacion.objects.all()
#     return render(request, 'Principal.html', {'proyecto': proyecto, 'presentaciones': presentaciones})


def contacto(request):
    data = {'form': Contactoform()}
    if request.method == 'POST':
        formulario = Contactoform(data=request.POST)
        if request.method.is_valid():
            formulario.save()
            data['mensaje'] = "Contacto Guardado"  
        else:
            data['form'] = formulario
    return render(request, 'portafolio/contacto.html',data)
    
    
def cv(request):
    # Obtenemos el CV del archivo
    cv = open("cv.pdf", "rb")

    # Enviamos el CV al navegador
    response = HttpResponse(cv, content_type="media/Portafolio/CV/CV.pdf")
    response = response.as_attachment(filename="CV.pdf")

    return response
