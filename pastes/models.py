from django.db import models
from django.contrib.auth.models import User




# userObjects =User.objects.all()
# userList= (tuple(zip([str(i) for i in userObjects],
#  [str(i) for i in userObjects])))
# print (userList)
# class Test(models.Model):
#     allowed = models.CharField(max_length=200, choices=userList, blank=True, null=True)
#     # paste = models.ForeignKey("pastes.Paste", on_delete=models.CASCADE, null = True, blank=True, related_name="permissions")
#     def __str__(self):
#         return self.allowed

class Paste(models.Model):
    name = models.CharField(max_length=200, default="Untitled")
    code=models.TextField()
    created= models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, default="anonymous")
    privacy = models.CharField(max_length=100)
    allow = models.ManyToManyField('auth.User',blank=True)
    def __str__(self):
        return self.name