from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class BoardUser(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=200)
    categories = models.ManyToManyField(Category, through="AdCategory")
    description = models.TextField()
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return f'{self.title}: {self.categories}'


class AdCategory(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.category


class Comment(models.Model):
    comment_text = models.TextField()
