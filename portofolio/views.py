from django.shortcuts import render
from .models import Experience, Education, Project


def home(request):
    return render(request, 'portofolio/home.html')

def experiences(request):
    experiences = Experience.objects.all()
    return render(request, 'portofolio/experiences.html', {'experiences': experiences})

def educations(request):
    educations = Education.objects.all()
    return render(request, 'portofolio/educations.html', {'educations': educations})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portofolio/projects.html', {'projects': projects})