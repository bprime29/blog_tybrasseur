from django import forms
from blog.models.post import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'desc', 'text',)
