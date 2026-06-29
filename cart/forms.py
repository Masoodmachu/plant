from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit
from cart.models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model=Payment
        fields=['id','name','amount']


