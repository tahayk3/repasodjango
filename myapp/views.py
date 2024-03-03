from django.shortcuts import render
#JsonResponse, su usa para transformar los datos y que le navegador lo pueda utilizar
from django.http import HttpResponse, JsonResponse

#se importan los modelos para poder responder en base a lo que realice el usuario
from . models import Project, Task

#para enviar a una pagina de error y que no se caiga el servidor se utiliza: 
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return HttpResponse("Index page")

def hello(request, nombreUsuario):
    print(nombreUsuario)
    return HttpResponse("<h1>Hello %s</h1>" %nombreUsuario)

def about(request):
    return HttpResponse("about")

def projects(request):
        #aqui se pueden realizar las consultas que se hacen  dn django shell
        #list(), convierte algo a una lista
        variableProjects = list(Project.objects.values())
        return JsonResponse(variableProjects,safe=False)

def tasks(request,id_task):
        #manejo sin la pagina 404}
        #task = Task.objects.get(id=id_task)
        
        #si no se encuentra el id, que muestre la pagina de error
        task = get_object_or_404(Task, id=id_task)
        return HttpResponse('Task: %s' % task.title)

