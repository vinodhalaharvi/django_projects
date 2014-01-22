# Create your views here.

from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout, login
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import Context, loader
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView
from post.models import Post, Comment


@login_required(login_url='/post/login/')
def post(request, post_id):
	if request.method == "GET":
		p = get_object_or_404(Post, pk=post_id)
		return render_to_response('post/templates/post.html', {'post': p},
			    context_instance=RequestContext(request))
	else:
		print request.POST
		comment = request.POST.get("comment")	
		if comment:
			c = Comment()
			c.post_id = post_id
			c.comment =  comment
			c.save()
			p = get_object_or_404(Post, pk=post_id)
			return render_to_response('post/templates/post.html', {'post': p},
				    context_instance=RequestContext(request))
		else:
			return HttpResponse("<strong>you must provide valid comment</strong>")



@login_required(login_url='/post/login/')
def index(request):
        post_list = Post.objects.all().order_by('-pub_date')[:5]
        t = loader.get_template('post/templates/index.html')
        c = Context({
                'post_list': post_list,
        })
        return HttpResponse(t.render(c))

@csrf_exempt
def login_view(request):
	if request.method == "GET":
		return render_to_response("post/templates/login.html")
	else:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect("/post/")
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
	return render_to_response("post/templates/login.html")


@login_required(login_url='/post/login/')
def content(request):
	"""docstring for content"""
	return render_to_response("post/templates/content.html")



