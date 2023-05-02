from django.urls import path

from . import views

app_name = 'meeting'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('<int:pk>', views.detail, name='detail'),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('<int:pk>/complete', views.complete, name='complete')
]