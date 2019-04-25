from home.models import Order
from django import forms
class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['full_name','oblis','city','description','author','method']
        widgets={
            "author": forms.HiddenInput(),
            "method": forms.HiddenInput(),
        }