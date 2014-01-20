from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout, login
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from crud.models import Book
from crud.forms import BookForm

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
				return redirect("list")
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
	object_list = (
			{ 'id':  100, 'attr1': 'attr1', 'attr2': 'attr2', }, 
			{ 'id':  101, 'attr1': 'attr1', 'attr2': 'attr2', }, 
			{ 'id':  102, 'attr1': 'attr1', 'attr2': 'attr2', }, 
		)
	return render_to_response("crud.html", {"objects_list": object_list})


def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
	    subject = form.cleaned_data['subject']
	    message = form.cleaned_data['message']
	    sender = form.cleaned_data['sender']
	    cc_myself = form.cleaned_data['cc_myself']

	    recipients = ['info@example.com']
	    if cc_myself:
		recipients.append(sender)

	    from django.core.mail import send_mail
	    send_mail(subject, message, sender, recipients)
	    return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render(request, 'contact.html', {
        'form': form,
    })


@login_required
def list(request, id=None):
	"""docstring for list"""
	if not id:
		books = Book.objects.all()
		return render_to_response("list.html", {"books":books})
	else:
		book = Book.objects.get(id = id)
		return render_to_response("list.html", {"books":[book]})

@login_required
@csrf_exempt
def update(request, id):
	"""docstring for update"""
	if request.method == 'GET':
		book = Book.objects.get(id=id)
		return render_to_response("update.html", {"book": book} )
	else:
	    if request.method == 'POST': # If the form has been submitted...
		form = BookForm(request.POST)
		if form.is_valid(): # All validation rules pass
			book = Book.objects.get(id=id)
			book.title = request.POST["title"]
			book.author = request.POST["author"]
			book.save()
			return redirect("list")


@login_required
@csrf_exempt
def new(request):
	"""docstring for new"""
	if request.method == "GET":
		form = BookForm(instance=Book())
		return render_to_response("new.html", {"form":form})
	else:
		form = BookForm(request.POST)
		if form.is_valid(): # All validation rules pass
			form.save()
			return redirect("list")
		else:
			return render_to_response("new.html", {"form":form, 
					"error": "INVALID FORM REQUEST"})

def deleteSelected(request, ids):
	"""docstring for deleteSelected"""
	if request.method == "POST":
		for id in ids:
			book = Book.objects.get(id = id )
			book.delete()
		return redirect("list")
	else:
		return redirect("list")


@login_required
def detail(request, id):
	"""docstring for detail"""
	book = Book.objects.get(pk=id)
	return render_to_response("detail.html", {"book": book})


@login_required
@csrf_exempt
def delete(request, id):
	"""docstring for delete"""
	if request.method == "POST":
		book = Book.objects.get(id = id )
		book.delete()
		return redirect("list")
	else:
		return redirect("list")
