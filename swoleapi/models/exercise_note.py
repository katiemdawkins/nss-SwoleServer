from django.db import models


class Exercise_Note(models.Model):
    description = models.CharField(max_length=300)
    exercise_in_session: models.ForeignKey("Exercise_In_Session", on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag", through="Note_Tag", related_name="exercise_notes")