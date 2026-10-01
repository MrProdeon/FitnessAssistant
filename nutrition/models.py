from django.db import models

from users.models import CustomUser


# Create your models here.

class NutritionShapshot(models.Model):
    user = models.ForeignKey(to=CustomUser, related_name="snapshots")

    added_at = models.DateTimeField(auto_now_add=True)

    basal_metabolic_rate = models.FloatField()
    protein_norm = models.FloatField()
    fat_norm = models.FloatField()
    calorie_norm = models.FloatField()

