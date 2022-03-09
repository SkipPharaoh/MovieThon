from django.contrib import admin
from .models import Comment, UserProfile

admin.site.register(Comment)
admin.site.register(UserProfile)
