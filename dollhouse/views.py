from django.http import HttpResponse
from django.shortcuts import render_to_response

# index page
def home(request):
	return render_to_response('index.html')

# image_sniffer page
def image_sniffer(request):
	return render_to_response('image_sniffer.html')