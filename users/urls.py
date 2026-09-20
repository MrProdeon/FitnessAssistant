from django.urls import path
from . import views
from users.apps import UsersConfig
from .views import UserListCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("", UserListCreateAPIView.as_view(), name="user-list-create")
]