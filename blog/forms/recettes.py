from django import forms
from blog.models.recettes import Recette, Etape, Ingredient, Photo
from django.forms.models import inlineformset_factory


class RecetteForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Recette
        fields = '__all__'


class EtapeCustomForm(forms.ModelForm):
    required_css_class = 'required'
    detail = forms.CharField(required=True, widget=forms.Textarea(attrs={'cols': 40, 'rows': 2}))

    class Meta:
        model = Etape
        fields = '__all__'


IngredientFormset = inlineformset_factory(Recette, Ingredient, can_delete=False, fields='__all__')
EtapeFormset = inlineformset_factory(Recette, Etape, form=EtapeCustomForm, can_delete=False, fields='__all__')
ImageFormset = inlineformset_factory(Recette, Photo, can_delete=False, fields='__all__')
