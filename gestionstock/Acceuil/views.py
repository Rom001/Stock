from django.shortcuts import render
from .models import Produit

# Create your views here.

def index(request):
	return render(request, 'Acceuil/index.html')

def categorie(request):
	return render(request, 'Acceuil/categorie.html')

def Stock(request):
	return render(request, 'Acceuil/Stock.html')

# Create your views here.

def produit(request):
	produits = Produit.objects.all()
	data = {'produits' : produits}
	return render(request, 'Acceuil/produit.html', data)