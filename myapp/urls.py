from django.urls import path
from . import views

urlpatterns = [
    path('portafolio/', views.portafolio, name ='portafolio'),
    path('proyectos/', views.proyectos, name ='proyectos'),
    path('proyectos/create/', views.create_proyecto, name ='create_proyecto'),
    path('proyectos/<int:proyecto_id>', views.proyecto_detail, name ='proyecto_detail'),
    path('proyectos/<int:proyecto_id>/delete', views.delete_proyecto, name ='delete_proyecto'),
]