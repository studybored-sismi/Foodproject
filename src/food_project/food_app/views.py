from django.shortcuts import render
from rest_framework import generics, filters
from food_app.models import Food
from food_app.serializers import FoodSerializer
from food_app.models import Question
from food_app.serializers import QuestionSerializer


#from . import serializers

class FoodAPIView(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter,)
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
