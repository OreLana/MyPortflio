from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.
def home_index(request):
    return render(request, 'projects/index.html', {})

def about_index(request):
    return render(request, 'projects/about.html', {})

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'projects/project_detail.html', context)