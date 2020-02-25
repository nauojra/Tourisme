# sendemail/forms.py
from django import forms
from .models import Contact,VisiteGuidee

class ContactForm(forms.ModelForm):
	class Meta:
		model=Contact
		fields=[
         'nom',
         'email',
         'message',

		]

class VisiteForm(forms.ModelForm):
	class Meta:
		model=VisiteGuidee
		fields=[
         'nom',
         'prenom',
         'email',
         'telephone',
         'cin',
         'nbr',
         'date',
         'message',

		]
