from django.shortcuts import render
from django.template.context_processors import request
from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_200_OK

from nutrition.models import NutritionShapshot
from nutrition.serializers import NutritionShapshotRequestSerializer, TefRequestSerializer, \
    StepsRequestSerializer, TrainCaloriesRequestSerializer, EatRequestSerializer

from nutrition.services import calculate_nutrition_summary, calculate_bmr, calculate_tef, calculate_calories_by_steps, \
    calculate_train_calorie, calculate_neat, calculate_eat


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

class CalculateBMRAPIView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        bmr = calculate_bmr(user)

        return Response({"bmr" : bmr})

class CalculateTEFAPIView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        input_serializer = TefRequestSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        validated = input_serializer.validated_data
        bmr = validated.get("bmr", 0)

        tef = calculate_tef(bmr)

        return Response({"tef" : tef})

class CalculateStepsCaloriesAPIView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        input_serializer = StepsRequestSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        steps = input_serializer.validated_data["steps"]

        steps_calories = calculate_calories_by_steps(user, steps)

        return Response({"steps_calories" : steps_calories})

class CalculateTrainCaloriesAPIView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        input_serializer = TrainCaloriesRequestSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        train_time = input_serializer.validated_data.get("train_time", 0)

        train_calories = calculate_train_calorie(user, train_time)

        return Response({"train_calories" : train_calories})

class CalculateNeatAPIView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        input_serializer = StepsRequestSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        steps = input_serializer.validated_data.get("steps", 0)

        neat = calculate_neat(user, steps)

        return Response({"neat" : neat})

class CalculateEatAPIView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        input_serializer = EatRequestSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        validated = input_serializer.validated_data
        eat = calculate_eat(user,
                            validated["steps"],
                            validated["train_time"])

        return Response({"eat" : eat})