from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from django.http import JsonResponse
from .forms import UserForm, TaskForm, EditTaskForm
from django.contrib.auth.models import User

@login_required
def index(request):

    user_id = request.user.id

    context = {
        'tasks': Task.objects.all().filter(user=user_id),
        'user_id': user_id,
        'status_list': Task.status_list
    }
    return render(request, 'index.html', context)


def new_user(request):

    form = UserForm(request.POST)
    if form.is_valid():
        new_user = User.objects.create_user(request.POST['username'], 
                                            request.POST['email'],
                                            request.POST['password'],
                                            first_name=request.POST['first_name'],
                                            last_name=request.POST['last_name'])
        new_user.save()
        return redirect("home")

@login_required
def new_task(request):
    form = TaskForm(request.POST)

    if form.is_valid():
        form.save(commit=True)

    return redirect('home')

@login_required
def task_info(request, user_id: int, task_id: int):
    user = get_object_or_404(User, id=user_id)
    task = get_object_or_404(Task, id=task_id)

    context = {
        'task': task,
        'user': user,
        'status_list': Task.status_list,
    }

    return render(request, 'task_details.html', context)

@login_required
def edit_task(request, task_id: int):
    task = get_object_or_404(Task, id=task_id)

    title = task.title
    created_at = task.created_at
    updated_at = task.updated_at
    user = task.user

    form = EditTaskForm(request.POST)

    if form.is_valid():
        task.status = form.cleaned_data['status']
        task.save()

    return redirect('task-details', user.id, task_id)

def list_tasks(request):
    out = {}
    tasks = Task.objects.all()

    for task in tasks:
        out[task.title] = { 'user':task.user.username,
                            'status':task.status,
                            'created_at':task.created_at,
                            'updated_at':task.updated_at}
    
    return JsonResponse(out)