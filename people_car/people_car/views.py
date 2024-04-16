from django.http import HttpResponse
from django.shortcuts import render

from .forms import PersonneForm, VoitureForm
from .models import Personne, Voiture

def personne (request):
    data={
        "id": 1,
        "nom": "Vladimir",
        "prenom": "PUTIN",
        "age": 71,
        "genre": "President"
    }
    return render(request, "personne.html", data)

def personne_ajout(request):
    p = Personne.objects.create(nom="Attila", prenom="The Hun", age=120, genre="Conquerant")
    p.save()
    return HttpResponse(p)

def personnes(request):
    if request.method == "GET":
        context = {
            "title":"personnes",
            "form" :PersonneForm(),
            "personnes" : Personne.objects.all()
        }
        return render (request, "personne.html", context)
    elif request.method == "POST":
        data = PersonneForm(request.POST)
        if data.is_valid():
            nom_form = data.cleaned_data.get("nom")
            prenom_form = data.cleaned_data.get("prenom")
            age_form = data.cleaned_data.get("age")
            personne = Personne.objects.create(nom=nom_form,prenom=prenom_form,age=age_form)
            personne.save()
            return HttpResponse("Ajout réussi")
        return HttpResponse("Ajout échoué")



def voitures(request):
    if request.method == "GET":
        context = {
            "title":"voitures",
            "form" :VoitureForm(),
            "voitures" : Voiture.objects.all()
        }
        return render (request, "personne.html", context)
    elif request.method == "POST":
        data = VoitureForm(request.POST)
        if data.is_valid():
            marque_form = data.cleaned_data.get("marque")
            matricule_form = data.cleaned_data.get("matricule")
            proprietaire_form = data.cleaned_data.get("proprietaire")
            voiture = Voiture.objects.create(marque=marque_form,matricule=matricule_form,proprietaire=proprietaire_form)
            voiture.save()
            return HttpResponse("Ajout réussi")
        return HttpResponse("Ajout échoué") 
