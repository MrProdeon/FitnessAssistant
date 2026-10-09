from django.urls import path
from . import views
from users.apps import UsersConfig
from .views import UserListCreateAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView, \
    BodyFatCalculateAPIView, LBMCalculateAPIView, WeightClassAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("", UserListCreateAPIView.as_view(), name="user-list-create"),
    path("detail/<int:pk>/", UserRetrieveAPIView.as_view(), name="user-detail"),
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="user-update"),
    path("delete/<int:pk>/", UserDestroyAPIView.as_view(), name="user-delete"),

    path("calculate_body_fat/", BodyFatCalculateAPIView.as_view(), name="calculate-bodyfat"),
    path("calculate_lbm/", LBMCalculateAPIView.as_view(), name="calculate-lbm"),
    path("calculate_weight_class/", WeightClassAPIView.as_view(), name="calculate-weightclass")

]
