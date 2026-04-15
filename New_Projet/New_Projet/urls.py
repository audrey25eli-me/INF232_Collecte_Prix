"""
URL configuration for New_Projet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
from main.views import collecter_donnees, success_page, tableau_bord

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', collecter_donnees, name='collecte'), # Page d'accueil = Formulaire
    path('succes/', success_page, name='success_page'),
    path('analyse/', tableau_bord, name='tableau_bord'), # Page des résultats
]
