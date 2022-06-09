from rest_framework import serializers
from swoleapi.models.body_part import Body_Part



class BodyPartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Body_Part
        fields = ("id", 'label')