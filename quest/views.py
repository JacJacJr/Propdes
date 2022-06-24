from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
#from django.utils.translation import ugettext as _

from .forms import QuestForm, RoomFormSet
from .models import Quest
from .constants import *

def quest_show(request, quest_id):
    quest = Quest.objects.get(id=quest_id)
    return render(request, 'description.html',{'quest': quest})

def quest_create(request):
    if request.method == 'POST':
        form = QuestForm(request.POST)
        formset = RoomFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            instace = form.save()
            for room_form in formset:
                room = room_form.save(commit=False)
                room.quest = instace
                room.save()
            return redirect(f'/quest/description/{instace.id}')
        else:
            return render(
            request, 
            'questionnaire.html', 
            {'form': form, 'formset': formset}
        )
    else:
        form = QuestForm()
        formset = RoomFormSet()
        return render(
            request, 
            'questionnaire.html', 
            {'form': form, 'formset': formset}
        )



"""
	def questionnaire(request):
# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Questionnarie(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
   # if a GET (or any other method) we'll create a blank form
    else:
        form = Questionnarie()
    return render(request, 'questionnaire.html', {'form': form})
#def description(request, pk):
#	return HttpResponse("Tutaj wyświetla się opis")
"""
