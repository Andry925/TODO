from django.db import models

# Create your models here.


class Tasks(models.Model):
    task = models.CharField(max_length=250)
    task_is_completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.task
