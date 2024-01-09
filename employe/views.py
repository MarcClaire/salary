from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Employe, Contrat
from .forms import EmployeForm, ContratForm
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    return render(request, 'index.html')

#cette fonction permet d'affichier la liste des employé
def liste(request):
    employe_object = Employe.objects.all()
    return render(request,'employe/list.html',{'employe_object':employe_object})


def form(request):
    return render(request, 'ajout_employe.html')

#Cette fonction permet d'ajouter un employé
def ajouter_employe(request):
    if request.method == 'POST':
        form = EmployeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('personel'))  
    else:
        form = EmployeForm()
    return render(request, 'employe/ajout_employe.html', {'form': form})

#Cette fonction permet de modier les informations d'un employé
def update_empl_data(request, id):
    if request.method== 'POST':
        employe= Employe.objects.get(pk=id)
        form = EmployeForm(request.POST, instance=employe)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('personel')) 
        
    else:
        employe = Employe.objects.get(pk=id)
        form = EmployeForm(instance=employe)
    return render(request, 'employe/update_employe.html', {'form':form} )



#Cette fonction permet de supprmer un employé
def delete_employe(request, id):
    if request.method=='POST':
        employe = Employe.objects.get(pk=id)
        employe.delete()
    return HttpResponseRedirect(reverse('personel'))

#cette fonction permetd'afficher la liste des contrat
def liste_contrat(request):
    contrats = Contrat.objects.all()
    return render(request,'contrat/liste_contrat.html', {'contrats': contrats})

#Cette fonction permt d'ajouter un contrat
def ajouter_contrat(request):
    if request.method == 'POST':
        form = ContratForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('contrat'))  
    else:
        form = ContratForm()
    return render(request, 'contrat/ajout_contrat.html', {'form': form})

#Cette fonction permet de supprmer un contrat
def delete_contrat(request, id):
    if request.method=='POST':
        contrat = Contrat.objects.get(pk=id)
        contrat.delete()
    return HttpResponseRedirect(reverse('contrat'))

#Cette fonction permet de modier les informations d'un contrat
# def update_contrat_data(request, id):
#     contrat = get_object_or_404(Contrat, pk=id)
#     #employe = get_object_or_404(Employe, pk=id)
#     if request.method== 'POST':
#             #contrat= Contrat.objects.get(pk=id)
#             form = ContratForm(request.POST, instance=contrat)
#             if form.is_valid():
#                 employe_id = form.cleaned_data['employe'].id
#                 employe = get_object_or_404(Employe, fk=employe_id)
#                 form.save()
#     else:
#         contrat = Contrat.objects.get(pk=id)
#         form = ContratForm(instance=contrat)
#     return render(request, 'contrat/update_contrat.html', {'form':form} )

def update_contrat_data(request, id):
    if request.method== 'POST':
        contrat= Contrat.objects.get(pk=id)
        form = ContratForm(request.POST, instance=contrat)
        if form.is_valid():
            # employe.id= form.cleaned_data['employe'].id
            # employe = get_object_or_404(Employe, pk=employe.id)
            form.save()
        
    else:
        contrat = Contrat.objects.get(pk=id)
        form = ContratForm(instance=contrat)
    return render(request, 'contrat/update_contrat.html', {'form':form} )
