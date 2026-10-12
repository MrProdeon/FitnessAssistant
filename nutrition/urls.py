from django.urls import path, include

import nutrition.apps
from nutrition.views import NutritionSnapshotCreateAPIView, CalculateBMRAPIView, CalculateTEFAPIView, \
    CalculateStepsCaloriesAPIView, CalculateTrainCaloriesAPIView

app_name = nutrition.apps.NutritionsConfig.name

urlpatterns = [
    path("get_summary/", NutritionSnapshotCreateAPIView.as_view(), name="nutrition-summary"),
    path("calculate_bmr/", CalculateBMRAPIView.as_view(), name="calculate-bmr"),
    path("calculate_tef/", CalculateTEFAPIView.as_view(), name="calculate-tef"),
    path("calculate_steps_calories/", CalculateStepsCaloriesAPIView.as_view(), name="calculate-stepscalories"),
    path("calculate_train_calories/", CalculateTrainCaloriesAPIView.as_view(), name="calculate-traincalories")


]