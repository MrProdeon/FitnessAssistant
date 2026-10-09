from django.urls import path, include

import nutrition.apps
from nutrition.views import NutritionSnapshotCreateAPIView

app_name = nutrition.apps.NutritionsConfig.name

urlpatterns = [
    path("get_summary", NutritionSnapshotCreateAPIView.as_view(), name="nutrition-summary"),

]