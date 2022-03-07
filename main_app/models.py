from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=50)
    comment = models.TextField(max_length=1000)



# Rate #
# class Rate(models.Model):
    

#     like = models.IntegerChoices(1, 2, 3, 4, 5)
