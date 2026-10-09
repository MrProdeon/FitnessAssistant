from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response

from users.models import CustomUser
from users.permissions import IsSelfOrAdmin
from users.serializers import CustomUserSerializer

from users.services import calculate_body_fat, get_lean_body_mass, get_weight_class


# Create your views here.

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = []

    def get_permissions(self):
        if self.request.method == "GET":
            return [IsAuthenticated()]
        return [AllowAny()]

class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, IsSelfOrAdmin]

class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, IsSelfOrAdmin]

class BodyFatCalculateAPIView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        try:
            body_fat = calculate_body_fat(user)
        except ValidationError as e:
            raise ValidationError(str(e))

        user.body_fat = body_fat
        user.save(update_fields=["body_fat"])

        return Response({"body_fat" : body_fat})

class LBMCalculateAPIView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        try:
            lbm = get_lean_body_mass(user)
        except ValidationError as e:
            raise ValidationError(str(e))

        user.lean_body_mass = lbm
        user.save(update_fields=["lean_body_mass"])

        return Response({"lean_body_mass" : lbm})

class WeightClassAPIView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        try:
            weight_class = get_weight_class(user)
        except ValidationError as e:
            raise ValidationError(str(e))

        user.weight_class = weight_class
        user.save(update_fields=["weight_class"])

        return Response({"weight_class" : weight_class})
