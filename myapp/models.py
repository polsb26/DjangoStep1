from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    #con la siguiente funcion se puede observar el nombre en el panel admin
    def __str__(self):
        return self.name
class Task(models.Model):
    
    tittle = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    def __str__(self):
        
        return self.tittle+ ' - ' + self.project.name