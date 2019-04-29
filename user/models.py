from django.contrib.auth.models import User
from django.db import models

import datetime

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.BigIntegerField()
    birth_date = models.DateField(default="YYYY-MM-DD")
    country = models.CharField(max_length=100)
    facebook_profile = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_image',blank=True)

    


