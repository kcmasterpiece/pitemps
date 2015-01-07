from django.shortcuts import render
from tempGraph.models import Readings

# Create your views here.
def home_page(request):
	latestReading = Readings.objects.latest()
	return render(request, 'home.html', {'temperature': latestReading.temp } )