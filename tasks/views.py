from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
def index(request):

    user_id = request.user.id

    context = {
        'tasks': Task.objects.all().filter(user=user_id)
    }
    return render(request, 'index.html', context)