# myapp/models.py

from django.db import models

class CarBrand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brand_logos/', blank=True, null=True)
    photo_url = models.URLField(blank=True, null=True)  # ← NEW FIELD

    def __str__(self):
        return self.name
