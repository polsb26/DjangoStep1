from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask
# Create your views here.

def index(request):
    """mediante el metodo render se puede renderizar un template llamando al templa
    de la carpeta templates de la siguiente forma:"""
    #template pass data, forma de pasar datos 
    tittle= 'DJANGO!'
    return render(request, 'index.html', {'tittle':tittle})
def hello(request,username):
    print(username)
    return HttpResponse("<h1> Hello %s </h1>"%username)

def about(request):
    username= 'Diego'
    return render(request, 'about.html',{'username':username})

def projects(request):
    projects= Project.objects.all()
    return render(request, 'projects.html', {'projects':projects})

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html',
    {'tasks':tasks})

def create_task(request):
   if request.method == 'GET':
       return render(request, 'create_task.html', {'form':CreateNewTask()})
   else:
       Task.objects.create(
           tittle=request.POST['tittle'],
           description=request.POST['description'],
           project_id=2
       )
       return redirect('/tasks/')
