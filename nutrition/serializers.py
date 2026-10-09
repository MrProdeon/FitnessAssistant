from rest_framework.serializers import ModelSerializer

from nutrition.models import NutritionShapshot

class NutritionShapshotSerializer(ModelSerializer):
    class Meta:
        model = NutritionShapshot
        fields = "__all__"