from django.urls import path
from . import views


urlpatterns = [
    path('', views.vblog, name="vblog")
    
]