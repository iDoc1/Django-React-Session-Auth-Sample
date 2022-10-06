from email.policy import default
from django.db import models
from django.contrib.auth.models import User  # Django provided User model

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 1:1 between User and UserProfile
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=25, default='')

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
