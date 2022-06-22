from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
#from django.utils.translation import ugettext as _

from .forms import QuestForm
from .models import Quest
from .constants import *
from .descriptions import EXAMPLE_DESCRIPTION

def quest_show(request, quest_id):
    quest = Quest.objects.get(id = quest_id)
    #return HttpResponse(TITLES + HEADER + FLAT + BUILDING + LOCALIZATION)
    return HttpResponse(EXAMPLE_DESCRIPTION)

def quest_create(request):
    if request.method == 'POST':
      form = QuestForm(request.POST)
      if form.is_valid():
        form.save()
        quest_id = Quest.objects.latest('id').id
        return redirect(f'/quest/description/{quest_id}')
    else:
        form = QuestForm() 
        return render(request, 'questionnaire.html', {'form': form})



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
