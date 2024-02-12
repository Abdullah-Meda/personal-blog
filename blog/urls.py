"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import portofolio.views

from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [

    path("admin/", admin.site.urls),
    path("", portofolio.views.home, name='home'),
    path("career", portofolio.views.experiences, name='experiences'),
    path("projects", portofolio.views.projects, name='projects'),
    path("education", portofolio.views.educations, name='educations'),

] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)