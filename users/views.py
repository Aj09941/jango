from django.shortcuts import render, get_object_or_404

# Create your views here.
def login(request):
	return render(request , 'users/user-login.html')

def signup(request):
	return render(request , 'users/user-register.html')