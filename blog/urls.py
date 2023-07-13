from django.urls import path
from . import views


urlpatterns = [
    path('', views.vblog, name="vblog"),
    path('<int:post_id>',views.detail, name='detail'),
]