from django.contrib import admin
from .models import Req,Dep,Course

# Register your models here.

admin.site.register(Dep)

admin.site.register(Req)

admin.site.register(Course)