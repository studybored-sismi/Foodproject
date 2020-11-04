from django.shortcuts import render
from rest_framework import generics, filters
from food_app.models import Food
from food_app.serializers import FoodSerializer

#from . import serializers

class FoodAPIView(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter,)
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
