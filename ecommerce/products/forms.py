from django import forms
from .models import Stores,Products


class StoreForm(forms.ModelForm):

    class Meta:
        model = Stores
        fields = '__all__'

class ProductsForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = ['store','name','location','price','manufactured_data','available']


