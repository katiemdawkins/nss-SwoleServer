from django.db import models
from django.contrib.auth.models import User

class Swole_User(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture_url = models.CharField(max_length=200, default="💪")
    