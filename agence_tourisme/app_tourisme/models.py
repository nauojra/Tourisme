from django.db import models
class Sondage(models.model):
	question = models.CharField(max_lenght=200)
	date_publication = models.DateTimeField()
class Reponse(models.model):
	sondage = models.ForeignKey(Sondage)
	choix = models.CharField(max_lenght=200)
	nb_votes=models.IntegerField()


# Create your models here.
