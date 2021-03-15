from django.db import models
from django.utils import timezone


class Todo(models.Model):
    todo_text = models.CharField(default="", max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    todo_status = models.BooleanField(default=False)

    def __str__(self):
        return self.todo_text
