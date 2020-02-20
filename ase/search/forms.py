from .models import Search
from django import forms

class SearchForm(forms.ModelForm):
    class Meta:
        model=Search
        fields=['target','result']
