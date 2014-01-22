# Create your views here.
from django.conf.urls import patterns, include, url
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import Context, loader
from django.template import RequestContext
from django.views.generic import DetailView, ListView
from post.models import Post, Comment

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

		
def index(request):
        post_list = Post.objects.all().order_by('-pub_date')[:5]
        t = loader.get_template('post/templates/index.html')
        c = Context({
                'post_list': post_list,
        })
        return HttpResponse(t.render(c))

