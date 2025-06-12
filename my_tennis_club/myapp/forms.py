from django import forms
from .models import CarBrand

class CarBrandForm(forms.ModelForm):
    class Meta:
        model = CarBrand
        fields = ['name', 'description', 'country', 'photo_url','logo', 'price']  # Add photo_url
