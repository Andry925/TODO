from django.contrib import admin
from .models import Tasks

# Register your models here.


class TasksAdmin(admin.ModelAdmin):
    list_display = ("task", "task_is_completed", "updated_at")


admin.site.register(Tasks, TasksAdmin)
