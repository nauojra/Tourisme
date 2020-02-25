from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm, VisiteForm
from apptourisme.models import Hotel,Contact


# Create your views here.
def index(request):
	print(request.headers)
	return render(request,"index.html",{})

def hotel(request):
	hotel= Hotel.objects.all()
	return render(request,'hotel.html',{ 'liste_Hotels': hotel })

def transport(request):
	return render(request,'transport.html' )

def activite(request):
    return render(request,'activite.html')

def restaurant(request):
    return render(request,'restaurant.html')

def Tanger(request):
	return render(request,'Tanger.html')

def Assilah(request):
	return render(request,'Assilah.html')

def Larache(request):
	return render(request,'Larache.html')




def Contact_Create_View(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=ContactForm()
    context = {'form':form}
    return render(request, "contact.html", context)
def Contact_detail_View(request):
    obj = Contact.objects.get(id=1)
    context = {'object':obj}

def Visite_Create_View(request):
    form1 = VisiteForm(request.POST or None)
    if form1.is_valid():
        form1.save()
        form1=VisiteForm()
    context = {'form1':form1}
    return render(request, "visite.html", context)
def Visite_detail_View(request):
    obj = Visite.objects.get(id=1)
    context = {'object':obj}
