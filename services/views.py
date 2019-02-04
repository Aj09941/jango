from django.shortcuts import render, get_object_or_404
from .models import Services, FeatureImages ,Events

# Create your views here.
def services(request):
	services = Services.objects
	return render(request, 'services.html', {'services':services} )
	
def services_detail(request, service_id):
	service_detail = Services.objects
	service_detail =  get_object_or_404(Services , pk=service_id )
	return render(request, 'services.html', {'services':service_detail})

def home(request):
	imageOne = FeatureImages.objects.all()
	event = Events.objects.all()
	context = {
		'imageOne':imageOne ,
	 	'events':event
		}
	return render(request,'index.html',context)

def report(request):
	return render(request, 'popreport.html')

def resources(request):
	return render(request, 'resources.html')

def smrpriceguide(request):
	return render(request, 'smrpriceguide.html')

def store(request):
	return render(request, 'store.html')

def events(request):
	event = Events.objects.all()
	return render(request, 'events.html', {'events':event})
