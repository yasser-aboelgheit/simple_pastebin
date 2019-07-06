from django.db import models
from django.contrib.auth.models import User




class Paste(models.Model):
    name = models.CharField(max_length=200, default="Untitled")
    code=models.TextField()
    created= models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, default="anonymous")
    privacy = models.CharField(max_length=100)
    allow = models.ManyToManyField('auth.User',blank=True)
    def __str__(self):
        return self.name