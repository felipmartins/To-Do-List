from django import forms
from .models import Task
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ["user",
                  "title",
                  "status"]

class EditTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ["status"]

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["username",
                  "password",
                  "email",
                  "first_name",
                  "last_name"]