from django.db import models

# Project Model
class Project(models.Model):
    title = models.CharField(max_length=100)  #Title of each project
    description = models.TextField()           # Description of each project
    technology = models.CharField(max_length=20) #Technology used fo reach project
    image = models.ImageField(upload_to='img')   #Image associated with eah project
