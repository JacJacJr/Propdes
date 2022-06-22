from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
#from django.utils.translation import ugettext as _

from .forms import QuestForm
from .models import Quest
from .constants import *
from .descriptions import get_example_desc

def quest_show(request, quest_id):
    description = get_example_desc(quest_id)
    print(description)
    return HttpResponse(description[0])
    #return render(request, 'description.html',{'quest': quest})

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
