from django.db import models
from django.conf import settings


class Priority(models.Model):
    priority_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    number_priority = models.CharField(max_length=50)


class Status(models.Model):
    status_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    status_priority = models.CharField(max_length=50)


class Tasks(models.Model):
    task_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    priority_id = models.ForeignKey(Priority, on_delete=models.PROTECT)
    status_id = models.ForeignKey(Status, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    date_creation = models.DateTimeField()
    date_begin = models.DateTimeField() 
    date_end = models.DateTimeField()