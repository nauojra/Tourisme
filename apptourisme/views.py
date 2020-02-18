from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


# Create your views here.
def index(request):
	print(request.headers)
	return render(request,"index.html",{})


import urllib

def Message_Create_View(request):
    Contact = Contact()
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            #----- form -----#
            
            message = request.POST['message']
            nom = request.POST['name']
            email = request.POST['email']
            recaptcha_response = request.POST.get('g-recaptcha-response')
            #---- captcha -----#
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            #---- process data  -----#
                         
    context = {'Contact':contact}
    return render(request, "my_app/contact.html", context)