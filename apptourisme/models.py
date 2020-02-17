from django.db import models


# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Hotel(models.Model):

    idHotel=models.AutoField(primary_key=True)
    nomHotel=models.CharField(max_length=50,null=False,blank=False,verbose_name="Nom de hotel")
    descriptionHotel=models.TextField(null=False,blank=False,verbose_name="description de Hotel")
    noteHotel=models.TextField(null=False,blank=False,verbose_name="note de Hotel")

    def __str__(self):
        return self.nomHotel+","+self.descriptionHotel+","+self.noteHotel
class Restaurant(models.Model):

    idRestaurant=models.AutoField(primary_key=True)
    nomRestaurant=models.CharField(max_length=50,null=False,blank=False,verbose_name="Nom de Restaurant")
    lieuRestaurant=models.CharField(max_length=50,null=False,blank=False,verbose_name="Nom de Restaurant")
    descriptionRestaurant=models.TextField(null=False,blank=False,verbose_name="description de Restaurant")
    noteRestaurant=models.TextField(null=False,blank=False,verbose_name="note de Restaurant")

    def __str__(self):
        return self.nomRestaurant+","+self.lieuRestaurant+","+self.descriptionRestaurant+","+self.noteRestaurant


class Contact(models.Model):
    class Meta:
        verbose_name='Contact'
        verbose_name_plural="messages des personnes"

    idContact=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=50,null=False,blank=False,verbose_name="Nom du visiteur")
    email=models.CharField(max_length=50,null=False,blank=False,verbose_name="Email du visiteur")
    message=models.TextField(null=False,blank=False,verbose_name="message")

    def __str__(self):
        return self.nom+","+self.message

class VisitGuidee(models.Model):

    idVisit=models.AutoField(primary_key=True)
    nomVisit=models.CharField(max_length=50,null=False,blank=False,verbose_name="Nom de visit")
    nomGuide=models.CharField(max_length=50,null=False,blank=False,verbose_name="Nom de guide")
    dateVisit=models.DateTimeField(blank=True, null=True,verbose_name="date de visit")
    lieuVisit=models.CharField(max_length=50,null=False,blank=False,verbose_name="lieu de visit")
    capaciteMax=models.CharField(max_length=50,null=False,blank=False,verbose_name="capacite max des visiteur")
    capaciteActuelle=models.CharField(max_length=50,null=False,blank=False,verbose_name="capacite actuelle des visiteur")
    commentaire=models.TextField(null=False,blank=False,verbose_name="commentaire")


    def __str__(self):
        return self.nomVisit+","+self.lieuVisit+","+self.dateVisit+","+self.nomGuide+","+self.capaciteMax+","+self.capaciteActuelle+","+self.commentaire
class Guidee(models.Model):

    idVisit=models.AutoField(primary_key=True)
    prenomGuide=models.CharField(max_length=50,null=False,blank=False,verbose_name="prenom de guide")
    nomGuide=models.CharField(max_length=50,null=False,blank=False,verbose_name="Nom de guide")
    ville=models.CharField(max_length=50,null=False,blank=False,verbose_name="ville de guide")
    adresse=models.CharField(max_length=50,null=False,blank=False,verbose_name="adresse de guide")
    tel=models.CharField(max_length=50,null=False,blank=False,verbose_name="telephone de guide")
    mail=models.CharField(max_length=50,null=False,blank=False,verbose_name="mail de guide")
    langues=models.CharField(max_length=50,null=False,blank=False,verbose_name="langues de guide")
    description=models.TextField(null=False,blank=False,verbose_name="description de guide")
    note=models.TextField(null=False,blank=False,verbose_name="note")



    def __str__(self):
    	return self.nomGuide+","+self.prenomGuide+","+self.ville+","+self.adresse+","+self.tel+","+self.mail+","+self.langues+","+self.description+","+self.note
class Activite(models.Model):

    idActivite=models.AutoField(primary_key=True)
    nomActivite=models.CharField(max_length=50,null=False,blank=False,verbose_name="nom  Activite")
    typeActivite=models.CharField(max_length=50,null=False,blank=False,verbose_name="type Activite")
    descriptionActivite=models.TextField(null=False,blank=False,verbose_name="description Activite")
    dateActivite=models.DateTimeField(blank=True, null=True,verbose_name="date Activite")
    lieuActivite=models.CharField(max_length=50,null=False,blank=False,verbose_name="lieu Activite ")
    
    def __str__(self):
    	return self.nomActivite+","+self.typeActivite+","+self.descriptionActivite+","+self.dateActivite+","+self.lieuActivite
class Transport(models.Model):

    idTransport=models.AutoField(primary_key=True)
    lienTransport=models.TextField(null=False,blank=False,verbose_name="lien ")
    typeTransport=models.CharField(max_length=50,null=False,blank=False,verbose_name="type de Transport")
    descriptionTransport=models.TextField(null=False,blank=False,verbose_name="description")
    def __str__(self):
    	return self.typeTransport+","+self.descriptionTransport+","+self.lienTransport
# Create your models here.
