from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import time

# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User, related_name='profile', unique=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_image", blank=True, null=True)
    about = models.CharField(blank=True, max_length=250)
    city = models.CharField(max_length=64)

    def __str__(self):
        return self.user 


class Comment(models.Model):

    body = models.TextField(max_length=350)
    user = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='social_comments')

    def __str__(self):
        return self.body

    def get_length(self):
        return time.strftime("%M:%S", time.gmtime(self.length))
    
    class Meta:
        ordering = ['-timestamp']




