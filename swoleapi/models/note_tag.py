from django.db import models


class Note_Tag(models.Model):
    note = models.ForeignKey("Exercise_Note", on_delete=models.CASCADE)
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE)