from email.errors import FirstHeaderLineIsContinuationDefect
from django.db import models


class Session(models.Model):
    user = models.ForeignKey("Swole_User", on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    rating = models.IntegerField(default=1)  
    is_complete = models.BooleanField(default=False)

#default=1 on rating? then clicking finish button updates is_complete and rating