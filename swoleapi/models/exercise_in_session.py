from django.db import models


class Exercise_In_Session(models.Model):
    exercise = models.ForeignKey("Exercise", on_delete=models.CASCADE)
    session = models.ForeignKey("Session", on_delete=models.CASCADE)
    set_number = models.IntegerField()
    load = models.IntegerField()
    reps = models.IntegerField()
    

    