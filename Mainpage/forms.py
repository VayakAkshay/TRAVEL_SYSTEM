from django import forms
from .models import CustomerData

class ImageForm(forms.ModelForm):
    class Meta:
        model = CustomerData
        fields = ["customer_img"]
        labels = {"customer_img": ""}