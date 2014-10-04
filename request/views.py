from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import NameForm

#
# index
#
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        return HttpResponseRedirect('/request/get_name')

#
# get_name
#
def request(request, subpage):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/request/thanks')

    # if a GET (or any other method) we'll create a blank form
    else:

        if subpage == 'thanks':
            return render(request, 'thanks.html', {})

        else:
            form = NameForm()
            return render(request, 'name.html', {'form': form, 'debug': [request, subpage]})
