from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    time_registered = models.DateTimeField(auto_now_add=True)

    def create_user(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)
        self.save()


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
