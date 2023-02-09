from django.db import models
from datetime import datetime, timedelta
# Create your models here.


class List(models.Model):
    title = models.CharField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


def due_date():
    return datetime.now() + timedelta(days=7)


class Item(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField(default=due_date())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"This item to list <{self.list.title}>"
