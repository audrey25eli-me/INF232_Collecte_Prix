from django.shortcuts import render, redirect
from .forms import RelevePrixForm

def collecter_donnees(request):
    if request.method == 'POST':
        form = RelevePrixForm(request.POST)
        if form.is_valid():
            form.save() # Enregistre directement dans la base de données
            return redirect('success_page') # Redirige vers une page de succès
    else:
        form = RelevePrixForm()
    
    return render(request, 'main/collecte.html', {'form': form})

def success_page(request):
    return render(request, 'main/success.html')

# Create your views here.
from django.shortcuts import render, redirect
from django.db.models import Avg, Max, Min, Count # <-- Nouveau import pour les calculs
from .forms import RelevePrixForm
from .models import RelevePrix # <-- Nouveau import pour accéder aux données

def collecter_donnees(request):
    if request.method == 'POST':
        form = RelevePrixForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('success_page') 
    else:
        form = RelevePrixForm()
    
    return render(request, 'main/collecte.html', {'form': form})

def success_page(request):
    return render(request, 'main/success.html')

# --- ICI TU AJOUTES LA SUITE POUR L'ANALYSE ---

def tableau_bord(request):
    # On récupère tous les prix enregistrés
    tous_les_releves = RelevePrix.objects.all()
    
    # On fait les calculs mathématiques (Analyse Descriptive)
    stats = RelevePrix.objects.aggregate(
        prix_moyen = Avg('prix'),
        prix_max = Max('prix'),
        prix_min = Min('prix'),
        total_collectes = Count('id')
    )
    
    context = {
        'releves': tous_les_releves,
        'stats': stats,
    }
    
    return render(request, 'main/tableau_bord.html', context)