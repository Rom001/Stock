from django.db import models

# Create your models here.

class Produit(models.Model):

	ID_produit = models.IntegerField()
	nom = models.CharField(max_length=40)

	def __str__(self):
		return self.nom