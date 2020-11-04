from rest_framework import serializers
#from . import models
from food_app.models import Question, Food
#from . models import Question

class QuestionSerializer(serializers.ModelSerializer):
   class Meta:
       model = Question
       fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
