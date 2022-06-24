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
       'number_of_building',
       'market',
       'flat_condition',
       'floor_area',
       'how_many_rooms',
       'price',
       'which_floor',
       'how_many_floors',
       'how_high',
       'why_flat_change',
       'atribute1',
       'atribute2',
       'atribute3',
       'type_of_building',
       'neigh_security',
       'building_condition',
       'with_equimpent',
       'when_move_out',
       'how_many_people',
       'flat_utilities',
       'flat_additional_spaces',
       'parking',
       'year_of_building',
       'building_facitilities',
       ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type_of_building'].widget = forms.RadioSelect()
        self.fields['type_of_building'].choices = TYPE_OF_BUILDING_CHOICES
        self.fields['flat_condition'].widget = forms.RadioSelect()
        self.fields['flat_condition'].choices = FLAT_CONDITION_CHOICES
        self.fields['parking'].widget = forms.RadioSelect()
        self.fields['parking'].choices = PARKING_CHOICES
        self.fields['market'].widget = forms.RadioSelect()
        self.fields['market'].choices = MARKET_CHOICES

        #jak to dopisywać

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            'type_of_room',
            'floor_area',
            'room_additional_space',
            'window_in_room',
        ]


RoomFormSet = formset_factory(RoomForm)