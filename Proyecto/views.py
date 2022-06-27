from django.http import HttpResponse
from django.template import Template
from django.template import Context
from Proyecto.models import familiar
from django.template import loader


def saludo(request):   #Nuestra primera vista :)
    
    template1 = loader.get_template("template1.html")
    flia = familiar (nombre = "delfina" , edad = 15 , fechanacimiento = "22.22")
    
    render1= template1.render({"flia":flia,})

    return HttpResponse(render1)



