from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return self.title
