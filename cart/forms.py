from django import forms

class AddToCartForm(forms.Form):
    QUANTITY_CHOICES = [(i , str(i)) for i in range(1, 11)]
    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES , coerce=int)
    inplace = forms.BooleanField(required=False , widget=forms.HiddenInput)