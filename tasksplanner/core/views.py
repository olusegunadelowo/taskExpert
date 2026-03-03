
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Taskn

# Create your views here.

def base(request):
    return render(request, 'core/base.html')


# The C aspect of CRUD
def create(request):
    if request.POST:
        title = request.POST.get('title')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        task = Taskn.objects.create(title=title,start_time=start_time,end_time=end_time)
        task.save()
        messages.success(request, f'Task: {task.title} created succesfully')
    tasks = Taskn.objects.all()
    context = {
        'tasks':tasks
    }
    return render(request, 'core/tasks.html', context)

# The U aspect of CRUD
def update(request, int):
    tasks = Taskn.objects.all()
    context = {
        'tasks':tasks
    }

    task = Taskn.objects.filter(id=int)
    if task.exists():
        task = task.first()
        print(task.is_expired)
        if task.is_expired == True:
            task.delete()
            messages.error(request, 'This task is already expired')
            return render(request, 'core/tasks.html', context)
        elif task.done == True:
            task.done = False
            task.save()
        else:
            task.done = True
            task.save()
            messages.success(request, f'Task: {task.title} completed succesfully')
    return render(request, 'core/tasks.html', context)

# The D aspect of CRUD
def delete(request, int):
    task = Taskn.objects.filter(id=int)
    if task.exists():
        task = task.first()
        task.delete()
        messages.success(request, f'Task: {task.title} deleted succesfully')
    tasks = Taskn.objects.all()
    context = {
        'tasks':tasks
    }
    return render(request, 'core/tasks.html', context)



