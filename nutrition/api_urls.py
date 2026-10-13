from django.urls import path, include

import nutrition.apps
from nutrition.api_views import NutritionSnapshotCreateAPIView, CalculateBMRAPIView, CalculateTEFAPIView, \
    CalculateStepsCaloriesAPIView, CalculateTrainCaloriesAPIView, CalculateNeatAPIView, CalculateEatAPIView, \
    CalculateCalorieNormAPIView, CalculateProteintNormAPIView, CalculateFatNormAPIView

app_name = "api-" + nutrition.apps.NutritionsConfig.name

urlpatterns = [
    path("get_summary/", NutritionSnapshotCreateAPIView.as_view(), name="nutrition-summary"),
    path("calculate_bmr/", CalculateBMRAPIView.as_view(), name="calculate-bmr"),
    path("calculate_tef/", CalculateTEFAPIView.as_view(), name="calculate-tef"),
    path("calculate_steps_calories/", CalculateStepsCaloriesAPIView.as_view(), name="calculate-stepscalories"),
    path("calculate_train_calories/", CalculateTrainCaloriesAPIView.as_view(), name="calculate-traincalories"),
    path("calculate_neat/", CalculateNeatAPIView.as_view(), name="calculate-neat"),
    path("calculate_eat/", CalculateEatAPIView.as_view(), name="calculate-eat"),
    path("calculate_calorie_norm_with_deficit/", CalculateCalorieNormAPIView.as_view(), name="calculate-calories-with-deficit"),
    path("calculate_protein_norm/", CalculateProteintNormAPIView.as_view(), name="calculate-proteinnorm"),
    path("calculate_fat_norm/", CalculateFatNormAPIView.as_view(), name="calculate-fatnorm")




]