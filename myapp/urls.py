#Este archivo no viene por defecto, se crea para que cada aplicacion tenga sus urls 
#De esa manera no se sobrecarga el archivo urls.py de mysite
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('about/', views.about),
]