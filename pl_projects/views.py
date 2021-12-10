import digitalocean

from django.shortcuts import render
from django.conf import settings

DIGITALOCEAN_ACCESS_TOKEN=settings.DIGITALOCEAN_ACCESS_TOKEN

# Create your views here.
def list_projects(request):
    manager = digitalocean.Manager(token=DIGITALOCEAN_ACCESS_TOKEN)
    my_projects = manager.get_all_projects()
    return render(request, 'list_projects.html', {'projects': my_projects})
