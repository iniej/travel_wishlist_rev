from django import forms
from .models import Place

# This creates a form object that is for entering data to go in a databaseself.

class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        '''These are the fields' name that get displayed on the home page'''
        fields = ('name', 'visited')


class PlaceInfoForm(forms.ModelForm):
    class Meta:
        model = Place
        '''These are the fields' name that are displayed on the place info form.'''
        fields = ('date_visited', 'comment')
