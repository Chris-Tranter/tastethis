from .models import JoinRequest
from django import forms


class JoinForm(forms.ModelForm):
    """ form creation """
    class Meta:
        model = JoinRequest
        fields = ('name', 'email', 'message')