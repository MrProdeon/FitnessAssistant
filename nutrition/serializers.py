from rest_framework import serializers

from nutrition.models import NutritionShapshot

class NutritionShapshotRequestSerializer(serializers.Serializer):
    steps = serializers.IntegerField(min_value=0)
    train_time = serializers.IntegerField(min_value=0)
    goal = serializers.ChoiceField(choices=["low", "medium", "agressive"], default="medium")

class TefRequestSerializer(serializers.Serializer):
    bmr = serializers.IntegerField(min_value=0)

class StepsRequestSerializer(serializers.Serializer):
    steps = serializers.IntegerField(min_value=0)

class TrainCaloriesRequestSerializer(serializers.Serializer):
    train_time = serializers.IntegerField(min_value=0)

class EatRequestSerializer(serializers.Serializer):
    steps = serializers.IntegerField(min_value=0)
    train_time = serializers.IntegerField(min_value=0)