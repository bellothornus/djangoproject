from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject
# Create your views here.


def home(request):
    # return HttpResponse("<h4>Hello World!</h4><a href='/about/'> About</a>")
    title = "Welcome to Django Course!"
    return render(request, 'index.html', {
        'title': title
    })


def about(request):
    # return HttpResponse("<p>About</p><a href='/' >volver</a>")
    username = 'divanov'
    return render(request, 'about.html', {
        'username': username
    })


def hello(request, username):
    print(username)
    return HttpResponse(f"<h4>Hello {username}!</h4><a href='/about/'> About</a>")


def hello_id(request, id):
    print(id)
    return HttpResponse(f"<h4>El id es: {id}!</h4><a href='/'> Volver</a>")


def projects(request):
    projects = list(Project.objects.all().values())
    # return JsonResponse(projects, safe=False)
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')

def tasks(request):
    # tasks = list(Task.objects.all().values())
    tasks = Task.objects.all()
    # return JsonResponse(projects, safe=False)
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })

def get_task_by_id(request, id):
    # tasks = list(Task.objects.filter(id=id).values())
    # return JsonResponse(tasks, safe=False)
    task = get_object_or_404(Task, id=id)
    # print(task.exists())
    # print(type(task))
    # print(task)
    return HttpResponse(f"Task: {task.title}")


def get_task_by_title(request, title):
    task = get_object_or_404(Task, title=title)
    return HttpResponse(f"Task: {task.title}")

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'],
                            description=request.POST['description'],
                            project_id=2)
        return redirect('tasks')

def project_detail(req, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=project.id)
    return render(req, 'projects/detail.html',{
        'project': project,
        'tasks': tasks
    })

def update_project(req,id):
    project = get_object_or_404(Project, id=id)
    

def remove_project(req, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect('projects')