from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'prod_name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'id': 'prod_price'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'id': 'prod_qty'}),
            'category': forms.Select(attrs={'class': 'form-select', 'id': 'prod_cat'}),
        }