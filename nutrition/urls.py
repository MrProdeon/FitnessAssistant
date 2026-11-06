from django.urls import path, include

from nutrition.views import NutritionSummaryView

app_name = "nutrition"

urlpatterns = [
    path("nutrition_summary",NutritionSummaryView.as_view(), name="nutrition-summary")
]