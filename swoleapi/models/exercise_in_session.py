from django.db import models


class Exercise_In_Session(models.Model):
    exercise = models.ForeignKey("Exercise", on_delete=models.CASCADE)
    session = models.ForeignKey("Session", on_delete=models.CASCADE, related_name="Exercises_in_Session")
    set_number = models.IntegerField()
    load = models.IntegerField()
    reps = models.IntegerField()
    

    