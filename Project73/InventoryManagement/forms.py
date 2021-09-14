from django import forms
from django.forms import widgets
from .models import Product


class ProductFormModel(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels ={
            'Product_name': 'Name of Product'
        }
        # widgets ={
        #     'Date': forms.SelectDateWidget
        # }