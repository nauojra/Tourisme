from django.shortcuts import render

# Create your views here.
def index(request):
	print(request.headers)
	return render(request,"index.html",{})