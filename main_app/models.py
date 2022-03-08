from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=50)
    comment = models.TextField(max_length=1000)



# Rate #
# class Rate(models.Model):

#     class Like(models.IntegerChoices):
#         NO = 0, _('No')
#         YES = 1, _('Yes')

