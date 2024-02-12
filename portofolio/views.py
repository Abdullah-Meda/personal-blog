from .models import Experience

from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'portofolio/home.html')

def experiences(request):
    experiences = Experience.objects.all()
    return render(request, 'portofolio/experiences.html', {'experiences': experiences})