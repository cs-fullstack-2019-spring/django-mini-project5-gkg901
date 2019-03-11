from django import forms
from .models import mealModel, userModel


class mealForm(forms.ModelForm):
    class Meta:
        model = mealModel
        exclude = ['creator']


class userForm(forms.ModelForm):
    class Meta:
        model = userModel
        exclude = ['userKey']
