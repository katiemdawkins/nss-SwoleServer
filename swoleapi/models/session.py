from django.db import models


class Session(models.Model):
    user = models.ForeignKey("Swole_User", on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    rating = models.IntegerField()  


    @property
    def exercisesInSession(self):
        return self.__exercisesInSession
    
    @exercisesInSession.setter
    def exercisesInSession(self, value):
        self.__exercisesInSession = value