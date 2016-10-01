from django.http import HttpResponse

# welcome message
def welcome(request):
	return HttpResponse("Welcome to DollHouse!")