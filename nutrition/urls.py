from django.urls import path, include

import nutrition.apps
from nutrition.views import NutritionSnapshotCreateAPIView, CalculateBMRAPIView

app_name = nutrition.apps.NutritionsConfig.name

urlpatterns = [
    path("get_summary", NutritionSnapshotCreateAPIView.as_view(), name="nutrition-summary"),
    path("calculate_bmr", CalculateBMRAPIView.as_view(), name="calculate-bmr")

]