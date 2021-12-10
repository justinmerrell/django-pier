
from django.urls import path, include

from pl_projects import views

urlpatterns = [
    path('projects', views.list_projects, name='list_projects'),
]
