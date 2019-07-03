from django.db import models

class Paste(models.Model):
    name = models.CharField(max_length=200, default="Untitled")
    code=models.TextField()
    created= models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name
