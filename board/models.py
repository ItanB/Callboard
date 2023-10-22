from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone


class BoardUser(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.username


class Ad(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment_text = models.TextField()
