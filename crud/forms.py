from django import forms
from django.forms import ModelForm
from crud.models import Book

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class BookForm(ModelForm):
	class Meta:
		model = Book
		fields = ["author", "title"]
