from django.contrib import admin

# Register your models here.
from .models import Task, Categories

admin.site.register(Task)
admin.site.register(Categories)