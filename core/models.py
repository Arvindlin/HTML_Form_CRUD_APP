from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Information(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    blog_title = models.CharField(max_length=50)
    email = models.EmailField(max_length=30, blank=True)
    blog = models.TextField()

    def __str__(self):
        return self.firstname


