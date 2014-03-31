from .models import Home, Service, About
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect

def home_page(request):
	return render_to_response('base.html', context_instance=RequestContext(request))