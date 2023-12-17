from django import forms
from .models import UserWebsite

class UserWebsiteForm(forms.ModelForm):
    class Meta:
        model = UserWebsite
        fields = ['name', 'url']

    widgets = {
        'name': forms.TextInput(attrs={'id': 'id_username'}),
    }
