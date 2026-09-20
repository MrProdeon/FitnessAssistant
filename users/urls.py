from django.urls import path
from . import views
from users.apps import UsersConfig
from .views import UserListCreateAPIView, UserRetrieveAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("", UserListCreateAPIView.as_view(), name="user-list-create"),
    path("<int:pk>/", UserRetrieveAPIView.as_view(), name="user-detail"),

]