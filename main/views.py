from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def user_login(request):
	next = request.GET.get('next', '/')
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user=authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(next)
			else:
				HttpResponse("Inactive user")
		else:
			return HttpResponseRedirect(settings.LOGIN_URL)
	return render(request, "main/login.html", {"redirect_to": next, "title": "Login"})
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(settings.LOGIN_URL)