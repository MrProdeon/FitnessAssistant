from django.urls import path, include

import nutrition.apps
from nutrition.views import NutritionSnapshotCreateAPIView

app_name = nutrition.apps.NutritionsConfig.name

urlpatterns = [
    path("create_snapshot/", NutritionSnapshotCreateAPIView.as_view(), name="create-snapshot"),

]