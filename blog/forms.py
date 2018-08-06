from django import forms
from .models import Post, Recette, Etape, Ingredient, Photo
from django.forms.models import inlineformset_factory


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'desc', 'text',)

class RecetteForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Recette
        fields = '__all__'


class calc_dens(forms.Form):
    di = forms.CharField(max_length=10)
    df = forms.CharField(max_length=10)
    sucre = forms.CharField(max_length=10)


class EtapeCustomForm(forms.ModelForm):
    required_css_class = 'required'
    detail = forms.CharField(required=True, widget=forms.Textarea(attrs={'cols': 40, 'rows': 2}))

    class Meta:
        model = Etape
        fields = '__all__'


IngredientFormset = inlineformset_factory(Recette, Ingredient, can_delete=False, fields = '__all__')
EtapeFormset = inlineformset_factory(Recette, Etape, form=EtapeCustomForm, can_delete=False, fields = '__all__')
ImageFormset = inlineformset_factory(Recette, Photo, can_delete=False, fields = '__all__')
