from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import index, new_task, new_user

urlpatterns = [
    path('', index, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='auth-login'),
    path("logout/", auth_views.LogoutView.as_view(template_name="login.html"), name="auth-logout",),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("new-user/", new_user, name="new-user"),
    path("new-task/", new_task, name="new-task"),
]
