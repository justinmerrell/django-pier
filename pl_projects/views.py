from os import environ, stat
import digitalocean

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

DIGITALOCEAN_ACCESS_TOKEN=settings.DIGITALOCEAN_ACCESS_TOKEN

# Create your views here.
def list_projects(request):
    manager = digitalocean.Manager(token=DIGITALOCEAN_ACCESS_TOKEN)
    my_projects = manager.get_all_projects()
    return render(request, 'list_projects.html', {'projects': my_projects})

def project_detail(request, project_id):
    manager = digitalocean.Manager(token=DIGITALOCEAN_ACCESS_TOKEN)
    project = manager.get_project(project_id)
    return render(request, 'project_details.html', {'project': project})

@csrf_exempt
def new_project(request):
    project_manager = digitalocean.Project(token=DIGITALOCEAN_ACCESS_TOKEN,
                            name=request.POST['name'], description=request.POST['description'],
                            purpose=request.POST['purpose'], environment=request.POST['environment']
                        )
    project = project_manager.create_project()
    return HttpResponse(project, status=200)
