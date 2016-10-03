from django.http import HttpResponse
from django.shortcuts import render_to_response

# welcome message
def welcome(request):
	return render_to_response('html/welcome.html')