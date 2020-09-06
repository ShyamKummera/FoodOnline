from django import forms
from pwn.models import StateModel,CityModel,CuisineModel,AdminLoginModel

class StateForm(forms.ModelForm):
    class Meta:
        model = StateModel
        fields = '__all__'

class CityForm(forms.ModelForm):
    class Meta:
        model = CityModel
        fields = '__all__'

class CuisineForm(forms.ModelForm):
    class Meta:
        model = CuisineModel
        fields = '__all__'

