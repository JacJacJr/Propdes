from django import forms

from .models import Flat, Space, Around
from .constants import *

        #jak tu wrzucić constans.py ?!!!!!!!!!!!!!!!!!!

class Quest(forms.Form):
    name_of_city = forms.CharField(label="name_of_city", max_length=50)

"""            
class FlatForm(forms.ModelForm):

    class Meta:
        model = Flat
        fields = ('name_of_city',)

class SpaceForm(forms.ModelForm):

    class Meta:
        model = Space
        fields = ('type_of_space',)

class AroundForm(forms.ModelForm):

    class Meta:
        model = Around
        fields = ('type_of_building',)
"""

