from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length= 500)
    image_url = models.CharField(max_length=200)
    body_part = models.ForeignKey("Body_Part", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    
    
    #custom property adding user id for create exercise
    @property
    def current_user(self):
        return self.__current_user
    
    @current_user.setter
    def current_user(self,value):
        self.__current_user=value