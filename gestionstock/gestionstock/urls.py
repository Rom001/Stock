from django.contrib import admin
from django.urls import path, include
from Acceuil import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Acceuil/', views.index, name='index'),
    path('Acceuil/Acceuil', views.index, name='index'),
    path('Acceuil/produit', views.produit, name='produit'),
    path('Acceuil/categorie', views.categorie, name='categorie'),
    path('Acceuil/Stock', views.Stock, name='Stock'),
]
