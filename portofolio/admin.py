from .models import Experience, Education, Project

from django.contrib import admin

# Register your models here.
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Experience)