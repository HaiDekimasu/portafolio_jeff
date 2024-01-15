from django.urls import path
from . import views



urlpatterns = [
    # path('', views.vporfolio, name="vporfolio"),
    path('contacto/', views.contacto, name="contacto"),
    path('model/', views.model, name="model")
]
