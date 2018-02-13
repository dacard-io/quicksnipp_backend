from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render #Import for rendering templates
from django.http import Http404 #Import 404s
from django.urls import reverse # For going back a page with forms
from django.views import generic # For generic class-based views
from django.conf import settings # Import settings.py for usage

# This is the index. I created a simple homepage view above
def index(request):
	template = loader.get_template('index.html')

	context = {} # Leave an empty context
	
	return HttpResponse(template.render(context, request))