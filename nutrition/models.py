from django.db import models
from django.db.models import CASCADE

from users.models import CustomUser


# Create your models here.

class NutritionShapshot(models.Model):
    user = models.ForeignKey(to=CustomUser, related_name="snapshots", on_delete=CASCADE)

    added_at = models.DateTimeField(auto_now_add=True)

    bmr = models.FloatField()
    protein_norm = models.FloatField()
    fat_norm = models.FloatField()
    calorie_norm_with_deficit = models.FloatField()

