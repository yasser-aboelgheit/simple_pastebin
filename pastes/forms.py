from django import forms
from . import models


class pasteform(forms.ModelForm):
    class Meta:
        model=models.Paste
        fields = ('name','code')