from django.shortcuts import render
from django.http import HttpResponse


def quest(request):
    return HttpResponse("Tutaj będą pola do wyboru")
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
