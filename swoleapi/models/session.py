from email.errors import FirstHeaderLineIsContinuationDefect
from django.db import models
from .exercise import Exercise


class Session(models.Model):
    user = models.ForeignKey("Swole_User", on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    rating = models.IntegerField(default=1)  
    is_complete = models.BooleanField(default=False)

#default=1 on rating? then clicking finish button updates is_complete and rating

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
    # @property
    # def average_rating(self):
    #     """Average rating calculated attribute for each session"""
    #     ratings = self.ratings.all()

    #     # Sum all of the ratings for sessions
    #     total_rating = 0
    #     for rating in ratings:
    #         total_rating += rating.rating

    #     # Calculate the averge and return it.
    #     ave_rating =0 
    #     if len(ratings) !=0:
    #         ave_rating = total_rating / len(ratings)
    #     #return the result
    #     return ave_rating