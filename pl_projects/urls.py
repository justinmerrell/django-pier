
from django.urls import path, include

from pl_projects import views

urlpatterns = [
    path('projects', views.list_projects, name='list_projects'),
    path('project/<project_id>', views.project_detail, name='project_detail'),

    path('new/project', views.new_project, name='new_project'),
]
