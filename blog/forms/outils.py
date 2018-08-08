from django import forms

class calc_dens(forms.Form):
    di = forms.CharField(max_length=4)
    df = forms.CharField(max_length=4)
    sucre = forms.CharField(max_length=4)
