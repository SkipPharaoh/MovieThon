from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import time

# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User, null=True, related_name='profile', unique=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/profile/", blank=True, null=True)
    about = models.TextField(blank=True, max_length=250)
    city = models.CharField(max_length=64)
    website = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    tiktok = models.CharField(max_length=255, null=True, blank=True)
    github = models.CharField(max_length=255, null=True, blank=True)
    discord = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)


class Comment(models.Model):

    body = models.TextField(max_length=350)
    user = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    likes = models.ManyToManyField(User, related_name='social_comments')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.body

    def get_length(self):
        return time.strftime("%M:%S", time.gmtime(self.length))
    
    class Meta:
        ordering = ['-timestamp']

class CommentSection(models.Model):
    comment = models.ForeignKey(Comment, related_name="comments", on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')

    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return '%s - %s' % (self.comment.body, self.name)



