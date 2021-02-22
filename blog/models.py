from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Category Model
class Category(models.Model):
    name = models.CharField(max_length=20) #Categories each post can have

    def __str__(self):
        return self.name

# Post Model
class Post(models.Model):
    title = models.CharField(max_length=100)  #Title of the post
    body = models.TextField()                 # Body of the post
    created_on = models.DateTimeField(default=timezone.now) #Time the post was created
    categories = models.ManyToManyField('Category', related_name='posts') #The categories for the post

    def __str__(self):
        return self.title
