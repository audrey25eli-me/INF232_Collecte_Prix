from django import forms
from .models import RelevePrix

class RelevePrixForm(forms.ModelForm):
    class Meta:
        model = RelevePrix
        # On choisit les champs que l'utilisateur doit remplir
        fields = ['produit', 'prix', 'marche', 'collecteur']
        
        # Pour mettre les labels en français
        labels = {
            'produit': 'Nom du produit',
            'prix': 'Prix constaté (FCFA)',
            'marche': 'Nom du marché',
            'collecteur': 'Votre nom',
        }