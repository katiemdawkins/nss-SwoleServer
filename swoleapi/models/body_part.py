from django.db import models


class Body_Part(models.Model):
    label = models.CharField(max_length=25)