from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.TextField(unique=False, blank=True, max_length=120)
    quantity = models.PositiveSmallIntegerField(unique=False, validators=[MinValueValidator(0), MaxValueValidator(100)])
