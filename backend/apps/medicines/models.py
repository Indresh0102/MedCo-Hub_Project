# backend/apps/medicines/models.py
from django.utils import timezone
from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    mg = models.PositiveIntegerField(null=True, blank=True)  # Optional field for milligrams
    expiry_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ({self.brand})"
