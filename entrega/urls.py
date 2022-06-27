
from django.contrib import admin
from django.urls import path
from Proyecto.views import saludo #Para acceder a la vista hay que importar el modulo y el método

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', saludo),   #ojo la url no hace falta que se llame saludo/ el nombre es libre, 
                                #pero la vista sí debe llamarse por su nombre

   
    
]