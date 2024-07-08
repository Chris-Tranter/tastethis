from .models import Recipe_comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Recipe_comment
        fields = ('comment',)