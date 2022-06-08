from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length= 500)
    image_url = models.CharField(max_length=200)
    body_part = models.ForeignKey("Body_Part", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)