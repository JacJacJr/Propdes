from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import QuestForm
from .models import *

def quest_create(request):
    if request.method == 'POST':
      form = QuestForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect('quest_create')
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
