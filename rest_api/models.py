from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    email = models.EmailField(default = '')
