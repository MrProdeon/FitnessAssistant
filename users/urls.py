from django.urls import path
from .views import RegisterView, Login, CalculateLBMView, CalculateWeightClassView
from django.contrib.auth.views import LogoutView
from users.views import CustomUserEditView, CalculateBodyFatView

app_name = "users"

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path("login/", Login.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("edit/<str:field>", CustomUserEditView.as_view(), name="profile-edit"),
    path("calculate_bodyfat/", CalculateBodyFatView.as_view(), name="calculate-bodyfat"),
    path("calculate_lbm/", CalculateLBMView.as_view(), name="calculate-lbm"),
    path("calculate_weight_class/", CalculateWeightClassView.as_view(), name="calculate-weight-class"),

]
