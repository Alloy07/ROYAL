from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from common.models import BaseModel


class Car(BaseModel):
    class GearType(models.TextChoices):
        MANUAL = 'manual'
        AUTO = 'auto'
        HYBRID = 'hybrid'

    name = models.CharField(max_length=100, null=False, blank=False)
    model = models.CharField(max_length=100, blank=True)
    description = models.TextField(null=False, blank=False)
    price = models.PositiveIntegerField(null=True, blank=True)
    brand = models.ForeignKey('cars.Brand', on_delete=models.CASCADE, related_name='cars')
    color = models.CharField(max_length=30)
    gear_type = models.CharField(max_length=10, choices=GearType.choices, default=GearType.MANUAL)
    distance_covered = models.PositiveIntegerField(null=True, blank=True)
    year = models.PositiveIntegerField(validators=[
        MinValueValidator(1986),  
        MaxValueValidator(2000) 
    ])
    def __str__(self):
        return self.name


class Brand(BaseModel):
    name = models.CharField(max_length=100, null=False, blank=False)   
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)


    def __str__(self):
        return self.name
    
