from django.contrib import admin
from django.urls import path
from Proyecto.views import saludo, mitemplate, prueba

urlpatterns = [
    path('admin/', admin.site.urls),
    path ("",saludo),
    path ("template/",mitemplate),
    path ("prueba/", prueba)
]
