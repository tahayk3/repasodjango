from django.db import models

# Create your models here.
#models.Model, es heredar los modejos de django
#un modelo no es mas que una clase de python que django transforma en una tabla
#Se esta creando una tabla con el nombre de Project

#TIPOS DE DATOS
# CharField es un string o varchar y max_length es la cantidad maxima de caracteres
# TextField se usa para textos largos
# Para crear relaciones entre tablas se utiliza ForeignKey(nombre de la tabla a relacionar)



#CORREN MIGRACIONES
#python manage.py makemigrations, busca las migraciones del proyecto nombreApp
#python manage.py migrate myapp, migra(crear tablas  o modificaciones de la estructura en db) 

class Project(models.Model):
    name = models.CharField(max_length=200)

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    #on_delete = models.cascade, elimina en cascada
    project = models.ForeignKey(Project,on_delete = models.CASCADE)



#con python manage.py shell, se puede realizar operaciones para modificar datos en las tablas de nuestra db
#En terminal, se ingresa el siguiente comando: python manage.py shell
    
#INSERTAR    
#from myapp.models import Project, Task
#p = Project(name="aplicacion movil")
#p.save()
    
#LISTAR
    #lista todos los objetos en la tabla
        #Project.objects.all()
    #lista un elemento en especifico en base a un parametro
        #Project.objects.get(id=1)
        #Project.objects.get(name="xd")

#INSERTAR       
    #para insertar en una tabla que tenga una relacion se realiza lo siguiente
    #se guarda en una variable el registro con el que voy a relacionar mi insersion
        #p = Project.objects.get(id="1")
    #luego se agregan los datos del registro, con la variable p
        #p.task_set.create(title="descargar IDE")
