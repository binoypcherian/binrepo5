from django.contrib import admin
from .models import Request, Department, Course
# Register your models here.

admin.site.register(Request)
admin.site.register(Department)
admin.site.register(Course)