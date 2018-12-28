from django import forms
from .models import Hubs


class HubsForm(forms.ModelForm):
    class Meta:
        model = Hubs
        fields = ('name',)


