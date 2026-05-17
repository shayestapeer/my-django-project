from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'myapp/task_list.html', {'tasks': tasks})
from django.shortcuts import redirect, get_object_or_404

def add_task(request):
    if request.method == "POST":
        title = request.POST['title']
        Task.objects.create(title=title)
        return redirect('task_list')
    return render(request, 'myapp/add_task.html')


def edit_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        task.title = request.POST['title']
        task.save()
        return redirect('task_list')

    return render(request, 'myapp/edit_task.html', {'task': task})


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('task_list')