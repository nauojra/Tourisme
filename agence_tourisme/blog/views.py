from django.shortcuts import render
from django.http import HttpResponse

def home(request):
        return HttpResponse("""
        <h1>Bienvenue sur mon blog!</h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
        """)
