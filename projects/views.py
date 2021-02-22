from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Views for the Projects App
def home_index(request):
    """View for the home page - renders 'index.html' """
    return render(request, 'projects/index.html', {})

def about_index(request):
    """View for the about page - renders 'about.html' """
    return render(request, 'projects/about.html', {})

def project_index(request):
    """View for the projects page - renders 'project_index.html' """
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/project_index.html', context)

def project_detail(request, pk):
    """View for each of the projects page accessed by their primary keys - renders 'project_detail.html' """
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'projects/project_detail.html', context)