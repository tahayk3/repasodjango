from django.contrib import admin

#Se utiliza para poder colocar en el panel de administracion, los modelos 
from .models import Project, Task

# Register your models here.
admin.site.register(Project)
admin.site.register(Task)

