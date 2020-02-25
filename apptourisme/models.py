from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone




class VisiteGuidee(models.Model):

    idVisite=models.AutoField(primary_key=True,default='')
    nom=models.CharField(max_length=10,null=False,blank=False,default='',verbose_name="Nom ")
    prenom=models.CharField(max_length=10,null=False,blank=False,default='',verbose_name="prenom")
    email=models.CharField(max_length=20,null=False,blank=False,default='',verbose_name="email")
    telephone=models.CharField(max_length=12,null=False,blank=False,default='',verbose_name="telephone")
    cin=models.CharField(max_length=10,null=False,blank=False,default='',verbose_name="cin")
    nbr=models.CharField(max_length=2,null=False,blank=False,default='',verbose_name="nombre des visiteur")
    date=models.CharField(max_length=10,null=False,blank=False,default='',verbose_name="date de visite")
    message=models.TextField(null=False,blank=False,default='',verbose_name="message")


    def __str__(self):
        return self.prenom+","+self.nom+","+self.email+","+self.telephone+","+self.cin+","+self.nbr+","+self.date+","+self.message


class Restaurant(models.Model):

    idRestaurant=models.AutoField(primary_key=True)
    nomRestaurant=models.CharField(max_length=50,null=False,blank=False,verbose_name="nom du Restaurant")
    lieuRestaurant=models.CharField(max_length=50,null=False,blank=False,verbose_name="lieu du Restaurant")
    descriptionRestaurant=models.TextField(null=False,blank=False,verbose_name="description du Restaurant")
    noteRestaurant=models.FloatField(null=False,blank=False,verbose_name="note du restaurant")
    lienRestaurant=models.CharField(max_length=300,null=False,blank=False,verbose_name=" lien du restaurant")

    def __str__(self):
        return self.nomRestaurant+","+self.lieuRestaurant+","+self.descriptionRestaurant+","+self.lienRestaurant


class Contact(models.Model):

    nom=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return self.nom+","+self.email+","+self.message

class Activite(models.Model):

    idActivite=models.AutoField(primary_key=True)
    nomActivite=models.CharField(max_length=50,null=False,blank=False,verbose_name="nom  Activite")
    typeActivite=models.CharField(max_length=50,null=False,blank=False,verbose_name="type Activite")
    descriptionActivite=models.TextField(null=False,blank=False,verbose_name="description Activite")
    dateActivite=models.DateTimeField(blank=True, null=True,verbose_name="date Activite")
    lieuActivite=models.CharField(max_length=50,null=False,blank=False,verbose_name="lieu Activite ")


    def __str__(self):
        return self.nomActivite+","+self.typeActivite+","+self.descriptionActivite+","+self.dateActivite+","+self.lieuActivite

class Hotel(models.Model):

    idHotel=models.AutoField(primary_key=True)
    nomHotel=models.CharField(max_length=50,null=False,blank=False,verbose_name="Nom de l'hotel")
    descriptionHotel=models.TextField(null=False,blank=False,verbose_name="description de l'hotel")
    noteHotel=models.FloatField(null=False,blank=False,verbose_name="note de l'hotel")
    lienHotel=models.CharField(max_length=300,null=False,blank=True,verbose_name=" lien de l'hotel")
    imageHotel=models.ImageField(upload_to='',null=True,blank=True,width_field="width_field",height_field="height_field")
    height_field=models.IntegerField(default=0)
    width_field=models.IntegerField(default=0)

    def __str__(self):
        return self.nomHotel+","+self.descriptionHotel
