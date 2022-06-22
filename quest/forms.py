from django import forms

from .models import Quest
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

"""!!!!!!!!! JAK ZROBIĆ żeby w formularzu pojawiał się RoomForm:
1. w ilości pokoi (for room in how_many_rooms)
2. z możliwością dodawania dowolnej ilości pomieszczeń (button "Dodaj")
"""            
# class FlatForm(forms.ModelForm):

#     class Meta:
#         model = Flat
#         fields = ('name_of_city',)

# class SpaceForm(forms.ModelForm):

#     class Meta:
#         model = Space
#         fields = ('type_of_space',)

# class AroundForm(forms.ModelForm):

#     class Meta:
#         model = Around
#         fields = ('type_of_building',)

