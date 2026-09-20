from django.urls import path
from . import views
from users.apps import UsersConfig
from .views import UserListCreateAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("", UserListCreateAPIView.as_view(), name="user-list-create"),
    path("detail/<int:pk>/", UserRetrieveAPIView.as_view(), name="user-detail"),
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="user-update"),
    path("delete/<int:pk>/", UserDestroyAPIView.as_view(), name="user-delete"),

]
