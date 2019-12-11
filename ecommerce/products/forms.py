from django import forms
from .models import Stores


class StoreForm(forms.ModelForm):

    class Meta:
        model = Stores
        fields = '__all__'


