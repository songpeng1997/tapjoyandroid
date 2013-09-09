""" Views for the base application """

from django.shortcuts import render
from django.http import HttpResponseRedirect

def home(request):
    """ Default view for the root """
    if request.mobile:
    	return HttpResponseRedirect('/m/')
    else:
    	return render(request, 'base/home.html')
