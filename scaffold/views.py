from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout, login
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@csrf_exempt
def login_view(request):
	if request.method == "GET":
		return render_to_response("login.html")
	else:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect("content")
			else:
				return HttpResponse(
					"<strong>YOUR ACCOUNT IS DISABLED!!</strong>", 
					content_type="text/html") 
		else:
			return HttpResponse("<strong>INVALID LOGIN</strong>", 
					content_type="text/html") 

@csrf_exempt
def logout_view(request):
	logout(request)
	return render_to_response("login.html")


@login_required
def content(request):
	"""docstring for content"""
	return render_to_response("content.html")

