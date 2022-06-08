from django.db import models


class Session(models.Model):
    user = models.ForeignKey("Swole_User", on_delete=models.CASCADE)
    exercise_in_session = models.ForeignKey("Exercise_In_Session", on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    rating = models.IntegerField()
    





#custom properties for set, reps, load??