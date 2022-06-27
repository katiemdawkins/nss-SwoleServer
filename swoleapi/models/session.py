from email.errors import FirstHeaderLineIsContinuationDefect
from django.db import models
from .exercise import Exercise


class Session(models.Model):
    user = models.ForeignKey("Swole_User", on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    rating = models.IntegerField(default=1)  
    is_complete = models.BooleanField(default=False)


    @property
    def currentExercises(self):
        return self.__currentExercises
    
    @currentExercises.setter
    def currentExercises(self,value):
        self.__currentExercises=value
    
    @property
    def averageRating(self):
        return self.__averageRating
    
    @averageRating.setter
    def averageRating(self,value):
        self.__averageRating=value 