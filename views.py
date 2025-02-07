# tasks/views.py

from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    """Display the list of tasks."""
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    """Handle adding a new task."""
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('task_list')
    return render(request, 'tasks/add_task.html')
