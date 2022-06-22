from django import forms
from django.forms import formset_factory

from .models import Quest, Room
from .constants import *

        #jak tu wrzucić constans.py ?!!!!!!!!!!!!!!!!!!

class QuestForm(forms.ModelForm):

    class Meta:
       model = Quest
       fields = [
       'name_of_city',
       'name_of_street', 
       'market',
       'floor_area',
       'how_many_rooms',
       'how_many_levels',
       'price',
       'which_flor',
       'how_many_flors',
       'flat_condition',
       'how_high',
       'flat_facilities',
       'why_flat_change',
       'type_of_building',
       'around_facilities',
       'around_security',
       'building_condition',
       ]


       # name_of_city = forms.CharField(label="name_of_city", max_length=50)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type_of_building'].widget = forms.RadioSelect()
        self.fields['type_of_building'].choices = TYPE_OF_BUILDING_CHOICES

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            'metrage',
        ]


RoomFormSet = formset_factory(RoomForm)