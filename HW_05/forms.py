from django import forms
from .models import Product

class ProductPhotoForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['photo']
