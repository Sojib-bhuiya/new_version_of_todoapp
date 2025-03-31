from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

from django.contrib.auth import authenticate, login, logout
from .models import Task

from .forms import TaskForm

# Create your views here.

@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user)
    # tasks = Task.objects.all()
    return render(request, 'todoapp/tasks_list.html', context={'tasks': tasks})


@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks')
    else:
        form = TaskForm()
        return render(request, 'todoapp/create_task.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_stuff = True
            user.save()
            login(request, user)
            return redirect('tasks')
    else:
        form = RegisterForm()
    return render(request, 'todoapp/register.html', {'form': form})

@login_required
def logoutPage(request):
    # user = request.user
    logout(request)
    return redirect('login')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    return HttpResponse('You cannot delete this task!')
    
@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todoapp/create_task.html', {'form': form})