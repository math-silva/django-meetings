from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('date/<str:op>/', views.date, name='date'),
    path('signup/', views.signup, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('users/', views.user_management_view, name='users'),
    path('remove_user/<int:pk>/', views.remove_user, name='remove_user'),
]