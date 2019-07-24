from django.contrib import admin
from .models import CoursePackage, CourseModule

# Register your models here.
admin.site.register(CoursePackage)
admin.site.register(CourseModule)
