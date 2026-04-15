from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=100) # ex: Sac de riz 25kg, Huile 1L
    categorie = models.CharField(max_length=50) # ex: Céréales, Liquides

    def __str__(self):
        return self.nom

class RelevePrix(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    prix = models.DecimalField(max_digits=10, decimal_places=2) # En FCFA
    marche = models.CharField(max_length=100) # ex: Marché central, Mokolo
    date_collecte = models.DateField(auto_now_add=True)
    collecteur = models.CharField(max_length=100) # Nom de la personne qui donne l'info

    def __str__(self):
        return f"{self.produit.nom} - {self.prix} FCFA"

# Create your models here.
