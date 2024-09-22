# from django.db import models
# from django.contrib.auth.models import AbstractUser


# # Create your models here.
# #Creating Custom User Model
# class CustomUser(AbstractUser):
#     bio = models.TextField(null=True, blank=True)
#     profile_picture = models.ImageField(null=True, blank=True)
#     followers = models.ManyToManyField('self', related_name='following', symmetrical=False, blank=True)

#     def __str__(self):
#         return self.username

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)

# symmetrical=False means if User A follows User B, it doesn't mean User B follows User A.

