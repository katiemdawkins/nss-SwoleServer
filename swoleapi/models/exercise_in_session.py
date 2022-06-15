from django.db import models
from datetime import datetime


class Exercise_In_Session(models.Model):
    exercise = models.ForeignKey("Exercise", on_delete=models.CASCADE, related_name = "Sessions")
    session = models.ForeignKey("Session", on_delete=models.CASCADE, related_name="Exercises_in_Session")
    set_number = models.IntegerField()
    load = models.IntegerField()
    reps = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    