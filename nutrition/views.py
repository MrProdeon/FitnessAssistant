from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from nutrition.models import NutritionShapshot
from nutrition.serializers import NutritionShapshotRequestSerializer

from nutrition.services import calculate_nutrition_summary

# Create your views here.

class NutritionSnapshotCreateAPIView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        input_serializer = NutritionShapshotRequestSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        validated = input_serializer.validated_data

        nutrition_summary = calculate_nutrition_summary(user=request.user,
                                                        steps=validated["steps"],
                                                        train_time=validated["train_time"],
                                                        goal=validated["goal"])

        return Response(nutrition_summary, status=status.HTTP_201_CREATED)