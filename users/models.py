from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Электронная почта должна быть обязательно указана")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_passord(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Супер-пользователь должен иметь is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Супер-пользователь должен иметь is_superuser=True")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):

    class Sex(models.TextChoices):
        MALE = "male", "Male"
        FEMALE = "female", "Female"

    class WeightClass(models.TextChoices):
        SLENDER = "slender", "Slender"
        EXCESS_WEIGHT = "excess weight", "Excess weight"
        OBESITY = "obesity", "Obesity"

    username = None
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефона", blank=True)
    email = models.EmailField(max_length=100, unique=True, blank=False, null=False)

    age = models.PositiveIntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    neck = models.FloatField(blank=True, null=True)
    waist = models.FloatField(blank=True, null=True)
    sex = models.CharField(max_length=6, choices=Sex.choices)
    hip = models.FloatField(blank=True, null=True)

    body_fat = models.FloatField(blank=True, null=True)
    lean_body_mass = models.FloatField(blank=True, null=True)
    weight_class = models.CharField(blank=True, null=True, choices=WeightClass.choices)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


